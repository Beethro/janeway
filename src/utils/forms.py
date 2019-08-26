from django.db.models import Prefetch

from django.forms import CharField, ModelForm, DateInput
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from hvad.forms import TranslatableModelForm

from submission import models as submission_models


class FakeModelForm(ModelForm):
    """ A form that can't be saved

    Usefull for rendering a sample form
    """

    def __init__(self, *args, disable_fields=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields = disable_fields
        if disable_fields is True:
            for field in self.fields:
                self.fields[field].widget.attrs["readonly"] = True

    def save(self, *args, **kwargs):
        raise NotImplementedError("FakeModelForm can't be saved")

    def clean(self, *args, **kwargs):
        if self.disable_fields is True:
            raise NotImplementedError(
                "FakeModelForm can't be cleaned: disable_fields is True",
            )
        return super().clean(*args, **kwargs)


class KeywordModelForm(ModelForm):
    """ A ModelForm for models implementing a Keyword M2M relationship """
    keywords = CharField(
            required=False, help_text=_("Hit Enter to add a new keyword."))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_keywords = self.instance.keywords.values_list("word", flat=True)
        field = self.fields["keywords"]
        field.initial = ",".join(current_keywords)

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=commit, *args, **kwargs)

        posted_keywords = self.cleaned_data.get('keywords', '').split(',')
        for keyword in posted_keywords:
            if keyword != '':
                obj, _ = submission_models.Keyword.objects.get_or_create(
                        word=keyword)
                instance.keywords.add(obj)

        for keyword in instance.keywords.all():
            if keyword.word not in posted_keywords:
                instance.keywords.remove(keyword)

        if commit:
            instance.save()
        return instance


class TranslatableKeywordModelForm(TranslatableModelForm):
    """ A ModelForm for models implementing a Keyword M2M relationship """
    #keywords = CharField(
    #        required=False, help_text=_("Hit Enter to add a new keyword."))

    def __init__(self, *args, **kwargs):
        self.language = kwargs.pop('language', get_language())
        self.keywords = kwargs.pop('keywords', None)
        super().__init__(*args, **kwargs)

        self.fields['keywords'] = CharField(
            required=False, help_text=_("Hit Enter to add a new keyword."))
        
        if self.keywords:
            self.fields['keywords'].initial = ",".join(self.keywords)
        else:
            self.fields['keywords'].initial = ""


    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=commit, *args, **kwargs)

        print(self.language)

        posted_keywords = self.cleaned_data.get('keywords', '').split(',')

        for keyword in posted_keywords:
            if keyword != '':
                obj, _ = submission_models.TransKeyword.objects.language(self.language).fallbacks('en').filter(word=keyword).get_or_create(word=keyword)
                                
                if not self.language in obj.get_available_languages():
                    obj.translate(self.language)
                obj.articles.add(instance)
                obj.save()

                instance.keywords.add(obj)

        for keyword in submission_models.TransKeyword.objects.language(self.language).fallbacks('en').filter(articles__id=instance.id):
            if keyword.word not in posted_keywords:
                instance.keywords.remove(keyword)
                keyword.articles.remove(instance)
                keyword.save()

        if commit:
            instance.save()
        return instance


class HTMLDateInput(DateInput):
    input_type = 'date'

__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"


from django import forms

from django_summernote.widgets import SummernoteWidget

from hvad.forms import TranslatableModelForm

from cms import models


class PageForm(TranslatableModelForm):

    class Meta:
        model = models.Page
        exclude = ('journal', 'is_markdown', 'content_type', 'object_id')

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)

        self.fields['content'].widget = SummernoteWidget()


class NavForm(TranslatableModelForm):

    class Meta:
        model = models.NavigationItem
        fields = ['link_name', 'link', 'is_external', 'sequence', 'page', 'has_sub_nav', 'top_level_nav', 'language']
        exclude = ('page', 'content_type', 'object_id')

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super(NavForm, self).__init__(*args, **kwargs)

        self.fields['top_level_nav'].queryset = models.NavigationItem.objects.language().fallbacks('en').filter(
            content_type=request.model_content_type,
            object_id=request.site_type.pk,
            has_sub_nav=True,
        )

__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"


from django.db import models
from django.utils import timezone


class Preprint(models.Model):
    article = models.ForeignKey('submission.Article', on_delete=models.CASCADE)
    doi = models.CharField(max_length=100)
    curent_version = models.IntegerField(default=1)

    def increase_version(self):
        self.curent_version = self.curent_version + 1
        self.save()


class PreprintVersion(models.Model):
    preprint = models.ForeignKey('submission.Article', on_delete=models.CASCADE)
    galley = models.ForeignKey('core.Galley', on_delete=models.CASCADE)
    version = models.IntegerField(default=1)
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_time', '-id')


class Comment(models.Model):
    author = models.ForeignKey('core.Account', on_delete=models.CASCADE)
    article = models.ForeignKey('submission.Article', on_delete=models.CASCADE)
    reply_to = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    date_time = models.DateTimeField(default=timezone.now)

    body = models.TextField(verbose_name='Write your comment:')

    is_reviewed = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_time', '-pk')

    def __str__(self):
        return 'Comment by {author} on {article}'.format(author=self.author.full_name(), article=self.article.title)


class Subject(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    editors = models.ManyToManyField('core.Account')
    preprints = models.ManyToManyField('submission.Article')
    enabled = models.BooleanField(default=True, help_text='If disabled, this subject will not appear publicly.')

    class Meta:
        ordering = ('slug', 'pk')

    def __str__(self):
        return self.name


def version_choices():
    return (
        ('correction', 'Correction'),
        ('version', 'New Version'),
    )


class VersionQueue(models.Model):
    article = models.ForeignKey('submission.Article', on_delete=models.CASCADE)
    galley = models.ForeignKey('core.Galley', on_delete=models.CASCADE)
    file = models.ForeignKey('core.File', on_delete=models.CASCADE)
    update_type = models.CharField(max_length=10, choices=version_choices())

    date_submitted = models.DateTimeField(default=timezone.now)
    date_decision = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False)

    def decision(self):
        if self.date_decision and self.approved:
            return True
        elif self.date_decision:
            return False

from django import template

from submission import models

register = template.Library()


@register.simple_tag
def get_issue_article_count(issue):
    return models.TransArticle.objects.language().fallbacks('en').filter(pk__in=issue.article_pks).length()
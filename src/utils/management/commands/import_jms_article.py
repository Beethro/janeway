from django.core.management.base import BaseCommand
from django.core import management

from utils.importers.up import import_in_review_article
from journal import models


class Command(BaseCommand):
    """
    Fetches a backend article from a UP journal
    """
    help = "Fetches a backend review article from a UP journal. Requires a journal code, a base url and an article id."

    def add_arguments(self, parser):
        """Adds arguments to Django's management command-line parser.

        :param parser: the parser to which the required arguments will be added
        :return: None
        """
        parser.add_argument('journal_code', default=None)
        parser.add_argument('base_url', default=None)
        parser.add_argument('article_id', default=None)
        parser.add_argument('auth_file', default=None)
        parser.add_argument('--nuke', action='store_true', dest='nuke')

    def handle(self, *args, **options):
        """Fetches a backend article from UP.

        :param args: None
        :param options: None
        :return: None
        """
        if options.get('nuke'):
            management.call_command('nuke_import_cache')

        url = '{base_url}/jms/editor/submission/{article_id}'.format(base_url=options.get('base_url'),
                                                                     article_id=options.get('article_id'))
        try:
            journal = models.Journal.objects.get(code=options.get('journal_code'))
            import_in_review_article(url,
                                     journal,
                                     auth_file=options.get('auth_file'),
                                     base_url=options.get('base_url'),
                                     article_id=options.get('article_id'))
        except models.Journal.DoesNotExist:
            print('Journal not found.')

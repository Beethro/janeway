__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"
from django.db import models
from django.utils import timezone


class ProductionAssignment(models.Model):
    article = models.OneToOneField('submission.Article')
    production_manager = models.ForeignKey('core.Account', null=True, on_delete=models.SET_NULL)
    editor = models.ForeignKey('core.Account', null=True, on_delete=models.SET_NULL, related_name='prod_editor')
    assigned = models.DateTimeField(default=timezone.now)
    notified = models.BooleanField(default=False)
    closed = models.DateField(blank=True, null=True)

    accepted_by_manager = models.ForeignKey('TypesetTask', null=True, blank=True)

    class Meta:
        unique_together = ('article', 'production_manager')

    def __str__(self):
        return 'PM Assignment {pk}'.format(pk=self.pk)

    def typeset_tasks(self):
        return self.typesettask_set.all()

    def active_typeset_tasks(self):
        return self.typesettask_set.filter(completed__isnull=True)

    def completed_typeset_tasks(self):
        return self.typesettask_set.filter(completed__isnull=False)


class TypesetTask(models.Model):
    assignment = models.ForeignKey(ProductionAssignment)
    typesetter = models.ForeignKey('core.Account', null=True, on_delete=models.SET_NULL)
    assigned = models.DateTimeField(default=timezone.now)
    notified = models.BooleanField(default=False)
    accepted = models.DateTimeField(blank=True, null=True)

    typeset_task = models.TextField(blank=True, null=True, verbose_name="Typesetting Task")
    files_for_typesetting = models.ManyToManyField('core.File', related_name='files_for_typesetting')
    galleys_loaded = models.ManyToManyField('core.File', related_name='galleys_loaded')
    note_from_typesetter = models.TextField(blank=True, null=True, verbose_name='Note to Editor')
    completed = models.DateTimeField(blank=True, null=True)

    editor_reviewed = models.BooleanField(default=False)

    @property
    def is_active(self):
        if self.assigned and not self.completed:
            return True
        else:
            return False

    @property
    def status(self):
        if self.assigned and not self.accepted and not self.completed:
            return "assigned"
        elif self.assigned and self.accepted and not self.completed:
            return "accepted"
        elif self.assigned and not self.accepted and self.completed:
            return "declined"
        elif self.completed and not self.editor_reviewed:
            return "completed"
        elif self.completed and self.editor_reviewed:
            return "closed"

    FRIENDLY_STATUSES = {
            "assigned": "Awaiting response",
            "accepted": "Task accepted",
            "declined": "Task declined",
            "completed": "Task completed",
            "closed": "Task closed",
        }

    @property
    def friendly_status(self):
        return self.FRIENDLY_STATUSES.get(self.status)

    def reset_task_dates(self):
        self.accepted = None
        self.completed = None
        self.editor_reviewed = False
        self.save()

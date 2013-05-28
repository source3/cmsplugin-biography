from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.alias import aliases
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

# Define aliases for easy_thumbnail
# See http://easy-thumbnails.readthedocs.org/en/latest/usage/#thumbnail-aliases
if not aliases.get('badge'):
    aliases.set('badge', {'size': (150, 80), 'crop': True})


class ActiveManager(models.Manager):
    """Returns objects with a field value of active=True."""
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active=True)


class PersonBiography(models.Model):
    """Stores biographical information about a Person."""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=250)
    suffix = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=250, blank=True)
    employer = models.CharField(max_length=250, blank=True)
    description = HTMLField()
    image = models.ImageField(upload_to='biography_person', blank=True)
    active = models.BooleanField(default=True,
        help_text=_('If checked, this biography will be available in the plugin list.'))

    active_objects = ActiveManager()

    class Meta:
        ordering = ('last_name', 'first_name', )
        verbose_name = 'Person biography'
        verbose_name_plural = 'Person biographies'

    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class PersonBiographyPluginModel(CMSPlugin):
    """
    Stores a reference to a PersonBiography. This is used so a given
    PersonBiography can be referenced by 0 or more PersonBiographyPlugins.
    """
    person = models.ForeignKey(PersonBiography)
    short_description = HTMLField(blank=True, help_text="If specified, this text will replace the person's normal description.")
    event_description = HTMLField(blank=True, help_text="If specified, this text will appear after the person's normal description.")

    class Meta:
        ordering = ('person', )

    def __unicode__(self):
        return unicode(self.person)

    def copy_relations(self, oldinstance):
        self.person = oldinstance.person


# Generate thumbnails when an image is uploaded.
saved_file.connect(generate_aliases_global)

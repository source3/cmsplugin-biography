from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import PersonBiographyPluginForm
from .models import PersonBiographyPluginModel


class PersonBiographyPlugin(CMSPluginBase):
    model = PersonBiographyPluginModel
    name = _('Biography -- Person')
    form = PersonBiographyPluginForm
    render_template = 'cmsplugin_biography/person.html'
    change_form_template = 'cmsplugin_biography/person_change_form.html'

    # If django-cms-search is being used, render the plugin and include
    # the text in the Haystack search index.
    search_fulltext = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['person'] = instance.person
        return context

plugin_pool.register_plugin(PersonBiographyPlugin)

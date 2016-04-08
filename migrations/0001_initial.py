# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PersonBiography'
        db.create_table(u'cmsplugin_biography_personbiography', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('employer', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('description', self.gf('djangocms_text_ckeditor.fields.HTMLField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'cmsplugin_biography', ['PersonBiography'])

        # Adding model 'PersonBiographyPluginModel'
        db.create_table(u'cmsplugin_personbiographypluginmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_biography.PersonBiography'])),
            ('short_description', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
            ('event_description', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_biography', ['PersonBiographyPluginModel'])


    def backwards(self, orm):
        # Deleting model 'PersonBiography'
        db.delete_table(u'cmsplugin_biography_personbiography')

        # Deleting model 'PersonBiographyPluginModel'
        db.delete_table(u'cmsplugin_personbiographypluginmodel')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_biography.personbiography': {
            'Meta': {'ordering': "('last_name', 'first_name')", 'object_name': 'PersonBiography'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {}),
            'employer': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        u'cmsplugin_biography.personbiographypluginmodel': {
            'Meta': {'ordering': "('person',)", 'object_name': 'PersonBiographyPluginModel', 'db_table': "u'cmsplugin_personbiographypluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'event_description': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsplugin_biography.PersonBiography']"}),
            'short_description': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_biography']
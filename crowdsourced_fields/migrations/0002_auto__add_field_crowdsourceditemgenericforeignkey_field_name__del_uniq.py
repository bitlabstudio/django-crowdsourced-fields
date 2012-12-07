# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'CrowdsourcedItemGenericForeignKey', fields ['item_type', 'object_id']
        db.delete_unique('crowdsourced_fields_crowdsourceditemgenericforeignkey', ['item_type', 'object_id'])

        # Adding field 'CrowdsourcedItemGenericForeignKey.field_name'
        db.add_column('crowdsourced_fields_crowdsourceditemgenericforeignkey', 'field_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CrowdsourcedItemGenericForeignKey.field_name'
        db.delete_column('crowdsourced_fields_crowdsourceditemgenericforeignkey', 'field_name')

        # Adding unique constraint on 'CrowdsourcedItemGenericForeignKey', fields ['item_type', 'object_id']
        db.create_unique('crowdsourced_fields_crowdsourceditemgenericforeignkey', ['item_type', 'object_id'])


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crowdsourced_fields.crowdsourceditem': {
            'Meta': {'object_name': 'CrowdsourcedItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_user_generated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '4000'})
        },
        'crowdsourced_fields.crowdsourceditemgenericforeignkey': {
            'Meta': {'object_name': 'CrowdsourcedItemGenericForeignKey'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdsourced_fields.CrowdsourcedItem']"}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['crowdsourced_fields']

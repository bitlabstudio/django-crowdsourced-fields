# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CrowdsourcedItemGenericForeignKey'
        db.create_table('crowdsourced_fields_crowdsourceditemgenericforeignkey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crowdsourced_fields.CrowdsourcedItem'])),
            ('item_type', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('crowdsourced_fields', ['CrowdsourcedItemGenericForeignKey'])

        # Adding unique constraint on 'CrowdsourcedItemGenericForeignKey', fields ['object_id', 'item_type']
        db.create_unique('crowdsourced_fields_crowdsourceditemgenericforeignkey', ['object_id', 'item_type'])

        # Adding model 'CrowdsourcedItem'
        db.create_table('crowdsourced_fields_crowdsourceditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_type', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('is_user_generated', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('crowdsourced_fields', ['CrowdsourcedItem'])


    def backwards(self, orm):
        # Removing unique constraint on 'CrowdsourcedItemGenericForeignKey', fields ['object_id', 'item_type']
        db.delete_unique('crowdsourced_fields_crowdsourceditemgenericforeignkey', ['object_id', 'item_type'])

        # Deleting model 'CrowdsourcedItemGenericForeignKey'
        db.delete_table('crowdsourced_fields_crowdsourceditemgenericforeignkey')

        # Deleting model 'CrowdsourcedItem'
        db.delete_table('crowdsourced_fields_crowdsourceditem')


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
            'Meta': {'unique_together': "(('object_id', 'item_type'),)", 'object_name': 'CrowdsourcedItemGenericForeignKey'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdsourced_fields.CrowdsourcedItem']"}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['crowdsourced_fields']
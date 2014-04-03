# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Senator.photo_url'
        db.add_column('idb_senator', 'photo_url',
                      self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Senator.photo_url'
        db.delete_column('idb_senator', 'photo_url')


    models = {
        'idb.bill': {
            'Meta': {'object_name': 'Bill'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'bill_set'", 'null': 'True', 'to': "orm['idb.Senator']", 'blank': 'True'}),
            'date_effective': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'date_proposed': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_session': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '70'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'primary_committee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'originating_committee_set'", 'null': 'True', 'to': "orm['idb.Committee']", 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '70'}),
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'voters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'voted_bill_set'", 'through': "orm['idb.Vote']", 'to': "orm['idb.Senator']", 'blank': 'True'})
        },
        'idb.committee': {
            'Meta': {'object_name': 'Committee'},
            'appointment_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'chair': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'committee_chair_set'", 'null': 'True', 'to': "orm['idb.Senator']", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'senators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'senator_set'", 'to': "orm['idb.Senator']", 'blank': 'True'}),
            'vice_chair': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'committee_vice_chair_set'", 'null': 'True', 'to': "orm['idb.Senator']", 'blank': 'True'})
        },
        'idb.senator': {
            'Meta': {'object_name': 'Senator'},
            'district': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_experience': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'map': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'occupation': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'photo_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'twitter': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'})
        },
        'idb.vote': {
            'Meta': {'object_name': 'Vote'},
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Bill']"}),
            'date_voted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'senator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Senator']"}),
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['idb']
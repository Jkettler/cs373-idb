# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Bill.primary_committee'
        db.alter_column('idb_bill', 'primary_committee_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idb.Committee'], on_delete=models.SET_NULL, null=True))

    def backwards(self, orm):

        # Changing field 'Bill.primary_committee'
        db.alter_column('idb_bill', 'primary_committee_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['idb.Committee']))

    models = {
        'idb.bill': {
            'Meta': {'object_name': 'Bill'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'bill_set'", 'symmetrical': 'False', 'blank': 'True', 'to': "orm['idb.Senator']", 'null': 'True'}),
            'date_effective': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'date_proposed': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_session': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'primary_committee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Committee']", 'related_name': "'bill_set'", 'on_delete': 'models.SET_NULL', 'blank': 'True', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'voters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'voted_bill_set'", 'symmetrical': 'False', 'blank': 'True', 'through': "orm['idb.Vote']", 'to': "orm['idb.Senator']"})
        },
        'idb.committee': {
            'Meta': {'object_name': 'Committee'},
            'appointment_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'chair': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Senator']", 'related_name': "'committee_chair_set'", 'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'senators': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'committee_set'", 'symmetrical': 'False', 'blank': 'True', 'to': "orm['idb.Senator']", 'null': 'True'}),
            'vice_chair': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Senator']", 'related_name': "'committee_vice_chair_set'", 'blank': 'True', 'null': 'True'})
        },
        'idb.picture': {
            'Meta': {'object_name': 'Picture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Senator']", 'related_name': "'pictures_set'", 'blank': 'True', 'null': 'True'})
        },
        'idb.senator': {
            'Meta': {'object_name': 'Senator'},
            'district': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_experience': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'map': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'idb.vote': {
            'Meta': {'object_name': 'Vote'},
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vote_set'", 'to': "orm['idb.Bill']"}),
            'date_voted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'senator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Senator']"}),
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['idb']
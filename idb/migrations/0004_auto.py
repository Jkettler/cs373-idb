# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field owners on 'Bill'
        db.delete_table(db.shorten_name('idb_bill_owners'))


    def backwards(self, orm):
        # Adding M2M table for field owners on 'Bill'
        m2m_table_name = db.shorten_name('idb_bill_owners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bill', models.ForeignKey(orm['idb.bill'], null=False)),
            ('senator', models.ForeignKey(orm['idb.senator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bill_id', 'senator_id'])


    models = {
        'idb.bill': {
            'Meta': {'object_name': 'Bill'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['idb.Senator']", 'null': 'True'}),
            'date_effective': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'date_proposed': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_session': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '70'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'primary_committee': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'originating_committee_set'", 'to': "orm['idb.Committee']", 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '70'}),
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'voters': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'voted_bill_set'", 'symmetrical': 'False', 'to': "orm['idb.Senator']", 'through': "orm['idb.Vote']"})
        },
        'idb.committee': {
            'Meta': {'object_name': 'Committee'},
            'appointment_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'chair': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'committee_chair_set'", 'to': "orm['idb.Senator']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'senators': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'senator_set'", 'symmetrical': 'False', 'to': "orm['idb.Senator']"}),
            'vice_chair': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'committee_vice_chair_set'", 'to': "orm['idb.Senator']", 'null': 'True'})
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
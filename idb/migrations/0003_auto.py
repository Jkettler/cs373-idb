# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field bills on 'Senator'
        db.delete_table(db.shorten_name('idb_senator_bills'))

        # Adding M2M table for field owners on 'Bill'
        m2m_table_name = db.shorten_name('idb_bill_owners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bill', models.ForeignKey(orm['idb.bill'], null=False)),
            ('senator', models.ForeignKey(orm['idb.senator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bill_id', 'senator_id'])


    def backwards(self, orm):
        # Adding M2M table for field bills on 'Senator'
        m2m_table_name = db.shorten_name('idb_senator_bills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('senator', models.ForeignKey(orm['idb.senator'], null=False)),
            ('bill', models.ForeignKey(orm['idb.bill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['senator_id', 'bill_id'])

        # Removing M2M table for field owners on 'Bill'
        db.delete_table(db.shorten_name('idb_bill_owners'))


    models = {
        'idb.bill': {
            'Meta': {'object_name': 'Bill'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['idb.Senator']", 'blank': 'True'}),
            'date_effective': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_proposed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_session': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'parent_set'", 'symmetrical': 'False', 'to': "orm['idb.Senator']", 'blank': 'True'}),
            'primary_committee': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'originating_committee_set'", 'to': "orm['idb.Committee']", 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'voters': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['idb.Vote']", 'related_name': "'voted_bill_set'", 'symmetrical': 'False', 'to': "orm['idb.Senator']", 'blank': 'True'})
        },
        'idb.committee': {
            'Meta': {'object_name': 'Committee'},
            'appointment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'chair': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'committee_chair_set'", 'to': "orm['idb.Senator']", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'senators': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'senator_set'", 'symmetrical': 'False', 'to': "orm['idb.Senator']", 'blank': 'True'}),
            'vice_chair': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'committee_vice_chair_set'", 'to': "orm['idb.Senator']", 'blank': 'True'})
        },
        'idb.senator': {
            'Meta': {'object_name': 'Senator'},
            'district': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Bill']"}),
            'date_voted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'senator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Senator']"}),
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['idb']

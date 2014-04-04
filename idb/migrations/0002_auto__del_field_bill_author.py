# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Bill.author'
        db.delete_column(u'idb_bill', 'author_id')

        # Adding M2M table for field bills on 'Senator'
        m2m_table_name = db.shorten_name(u'idb_senator_bills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('senator', models.ForeignKey(orm[u'idb.senator'], null=False)),
            ('bill', models.ForeignKey(orm[u'idb.bill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['senator_id', 'bill_id'])


    def backwards(self, orm):
        # Adding field 'Bill.author'
        db.add_column(u'idb_bill', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['idb.Senator'], null=True, related_name='authored_bill_set'),
                      keep_default=False)

        # Removing M2M table for field bills on 'Senator'
        db.delete_table(db.shorten_name(u'idb_senator_bills'))


    models = {
        u'idb.bill': {
            'Meta': {'object_name': 'Bill'},
            'date_effective': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_proposed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_session': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'primary_committee': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'originating_committee_set'", 'null': 'True', 'to': u"orm['idb.Committee']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'voters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'voted_bill_set'", 'blank': 'True', 'through': u"orm['idb.Vote']", 'to': u"orm['idb.Senator']"})
        },
        u'idb.committee': {
            'Meta': {'object_name': 'Committee'},
            'appointment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'chair': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'committee_chair_set'", 'null': 'True', 'to': u"orm['idb.Senator']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'senators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'senator_set'", 'blank': 'True', 'to': u"orm['idb.Senator']"}),
            'vice_chair': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'committee_vice_chair_set'", 'null': 'True', 'to': u"orm['idb.Senator']"})
        },
        u'idb.senator': {
            'Meta': {'object_name': 'Senator'},
            'bills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'bill_set'", 'blank': 'True', 'to': u"orm['idb.Bill']"}),
            'district': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_experience': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'map': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'idb.vote': {
            'Meta': {'object_name': 'Vote'},
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['idb.Bill']"}),
            'date_voted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'senator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['idb.Senator']"}),
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['idb']
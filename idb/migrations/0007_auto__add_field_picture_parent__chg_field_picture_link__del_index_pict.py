# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Picture.parent'
        db.add_column('idb_picture', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['idb.Senator'], blank=True),
                      keep_default=False)


        # Renaming column for 'Picture.link' to match new field type.
        db.rename_column('idb_picture', 'link_id', 'link')
        # Changing field 'Picture.link'
        db.alter_column('idb_picture', 'link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))
        # Removing index on 'Picture', fields ['link']
        db.delete_index('idb_picture', ['link_id'])


    def backwards(self, orm):
        # Adding index on 'Picture', fields ['link']
        db.create_index('idb_picture', ['link_id'])

        # Deleting field 'Picture.parent'
        db.delete_column('idb_picture', 'parent_id')


        # Renaming column for 'Picture.link' to match new field type.
        db.rename_column('idb_picture', 'link', 'link_id')
        # Changing field 'Picture.link'
        db.alter_column('idb_picture', 'link_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idb.Senator'], null=True))

    models = {
        'idb.bill': {
            'Meta': {'object_name': 'Bill'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'bill_set'", 'null': 'True', 'to': "orm['idb.Senator']", 'symmetrical': 'False', 'blank': 'True'}),
            'date_effective': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_proposed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_session': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'primary_committee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'originating_committee_set'", 'null': 'True', 'to': "orm['idb.Committee']", 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'voters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'voted_bill_set'", 'through': "orm['idb.Vote']", 'to': "orm['idb.Senator']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'idb.committee': {
            'Meta': {'object_name': 'Committee'},
            'appointment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'chair': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'committee_chair_set'", 'null': 'True', 'to': "orm['idb.Senator']", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'senators': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'senator_set'", 'to': "orm['idb.Senator']", 'symmetrical': 'False', 'blank': 'True'}),
            'vice_chair': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'committee_vice_chair_set'", 'null': 'True', 'to': "orm['idb.Senator']", 'blank': 'True'})
        },
        'idb.picture': {
            'Meta': {'object_name': 'Picture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['idb.Senator']", 'blank': 'True'})
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
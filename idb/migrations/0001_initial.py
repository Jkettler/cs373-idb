# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Senator'
        db.create_table('idb_senator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('party', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('occupation', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('legislative_experience', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('district', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50)),
            ('facebook', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200)),
            ('map', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('idb', ['Senator'])

        # Adding model 'Committee'
        db.create_table('idb_committee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('appointment_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('chair', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['idb.Senator'], related_name='committee_chair_set', blank=True)),
            ('vice_chair', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['idb.Senator'], related_name='committee_vice_chair_set', blank=True)),
        ))
        db.send_create_signal('idb', ['Committee'])

        # Adding M2M table for field senators on 'Committee'
        m2m_table_name = db.shorten_name('idb_committee_senators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('committee', models.ForeignKey(orm['idb.committee'], null=False)),
            ('senator', models.ForeignKey(orm['idb.senator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['committee_id', 'senator_id'])

        # Adding model 'Bill'
        db.create_table('idb_bill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('legislative_session', self.gf('django.db.models.fields.CharField')(blank=True, max_length=70)),
            ('date_proposed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_signed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_effective', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(blank=True, max_length=70)),
            ('url', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['idb.Senator'], related_name='authored_bill_set', blank=True)),
            ('primary_committee', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['idb.Committee'], blank=True)),
        ))
        db.send_create_signal('idb', ['Bill'])

        # Adding model 'Vote'
        db.create_table('idb_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('senator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idb.Senator'])),
            ('bill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idb.Bill'])),
            ('vote', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('date_voted', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('idb', ['Vote'])


    def backwards(self, orm):
        # Deleting model 'Senator'
        db.delete_table('idb_senator')

        # Deleting model 'Committee'
        db.delete_table('idb_committee')

        # Removing M2M table for field senators on 'Committee'
        db.delete_table(db.shorten_name('idb_committee_senators'))

        # Deleting model 'Bill'
        db.delete_table('idb_bill')

        # Deleting model 'Vote'
        db.delete_table('idb_vote')


    models = {
        'idb.bill': {
            'Meta': {'object_name': 'Bill'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['idb.Senator']", 'related_name': "'authored_bill_set'", 'blank': 'True'}),
            'date_effective': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_proposed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative_session': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '70'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'primary_committee': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['idb.Committee']", 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '70'}),
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'voters': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'through': "orm['idb.Vote']", 'to': "orm['idb.Senator']", 'symmetrical': 'False', 'related_name': "'voted_bill_set'"})
        },
        'idb.committee': {
            'Meta': {'object_name': 'Committee'},
            'appointment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'chair': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['idb.Senator']", 'related_name': "'committee_chair_set'", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'senators': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['idb.Senator']", 'symmetrical': 'False', 'related_name': "'senator_set'"}),
            'vice_chair': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['idb.Senator']", 'related_name': "'committee_vice_chair_set'", 'blank': 'True'})
        },
        'idb.senator': {
            'Meta': {'object_name': 'Senator'},
            'district': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'date_voted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'senator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idb.Senator']"}),
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['idb']
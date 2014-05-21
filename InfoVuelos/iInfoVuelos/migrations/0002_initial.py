# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Airport'
        db.create_table(u'iInfoVuelos_airport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.TextField')(max_length=3)),
            ('city', self.gf('django.db.models.fields.TextField')(max_length=100)),
        ))
        db.send_create_signal(u'iInfoVuelos', ['Airport'])

        # Adding model 'Company'
        db.create_table(u'iInfoVuelos_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.TextField')(max_length=2)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'iInfoVuelos', ['Company'])

        # Adding M2M table for field airport on 'Company'
        m2m_table_name = db.shorten_name(u'iInfoVuelos_company_airport')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'iInfoVuelos.company'], null=False)),
            ('airport', models.ForeignKey(orm[u'iInfoVuelos.airport'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'airport_id'])

        # Adding model 'Flight'
        db.create_table(u'iInfoVuelos_flight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.TextField')(max_length=5)),
            ('origin', self.gf('django.db.models.fields.TextField')(max_length=3)),
            ('destination', self.gf('django.db.models.fields.TextField')(max_length=3)),
            ('gate', self.gf('django.db.models.fields.TextField')(max_length=3)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'iInfoVuelos', ['Flight'])

        # Adding M2M table for field company on 'Flight'
        m2m_table_name = db.shorten_name(u'iInfoVuelos_flight_company')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('flight', models.ForeignKey(orm[u'iInfoVuelos.flight'], null=False)),
            ('company', models.ForeignKey(orm[u'iInfoVuelos.company'], null=False))
        ))
        db.create_unique(m2m_table_name, ['flight_id', 'company_id'])


    def backwards(self, orm):
        # Deleting model 'Airport'
        db.delete_table(u'iInfoVuelos_airport')

        # Deleting model 'Company'
        db.delete_table(u'iInfoVuelos_company')

        # Removing M2M table for field airport on 'Company'
        db.delete_table(db.shorten_name(u'iInfoVuelos_company_airport'))

        # Deleting model 'Flight'
        db.delete_table(u'iInfoVuelos_flight')

        # Removing M2M table for field company on 'Flight'
        db.delete_table(db.shorten_name(u'iInfoVuelos_flight_company'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'iInfoVuelos.airport': {
            'Meta': {'object_name': 'Airport'},
            'city': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'code': ('django.db.models.fields.TextField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '100'})
        },
        u'iInfoVuelos.company': {
            'Meta': {'object_name': 'Company'},
            'airport': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['iInfoVuelos.Airport']", 'symmetrical': 'False'}),
            'code': ('django.db.models.fields.TextField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'iInfoVuelos.flight': {
            'Meta': {'object_name': 'Flight'},
            'code': ('django.db.models.fields.TextField', [], {'max_length': '5'}),
            'company': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['iInfoVuelos.Company']", 'symmetrical': 'False'}),
            'destination': ('django.db.models.fields.TextField', [], {'max_length': '3'}),
            'gate': ('django.db.models.fields.TextField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.TextField', [], {'max_length': '3'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['iInfoVuelos']
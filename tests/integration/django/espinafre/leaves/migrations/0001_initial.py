# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Spinach'
        db.create_table('leaves_spinach', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('leaves', ['Spinach'])


    def backwards(self, orm):
        
        # Deleting model 'Spinach'
        db.delete_table('leaves_spinach')


    models = {
        'leaves.spinach': {
            'Meta': {'object_name': 'Spinach'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['leaves']

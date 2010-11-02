# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Spinach.color'
        db.add_column('leaves_spinach', 'color', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Spinach.color'
        db.delete_column('leaves_spinach', 'color')


    models = {
        'leaves.spinach': {
            'Meta': {'object_name': 'Spinach'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['leaves']

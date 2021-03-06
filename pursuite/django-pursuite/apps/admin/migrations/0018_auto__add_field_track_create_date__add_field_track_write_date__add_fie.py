# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Track.create_date'
        db.add_column(u'admin_track', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Track.write_date'
        db.add_column(u'admin_track', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Company.create_date'
        db.add_column(u'admin_company', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Company.write_date'
        db.add_column(u'admin_company', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Institution.create_date'
        db.add_column(u'admin_institution', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Institution.write_date'
        db.add_column(u'admin_institution', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SubSector.create_date'
        db.add_column(u'admin_subsector', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SubSector.write_date'
        db.add_column(u'admin_subsector', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Occupation.create_date'
        db.add_column(u'admin_occupation', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Occupation.write_date'
        db.add_column(u'admin_occupation', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Sector.create_date'
        db.add_column(u'admin_sector', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Sector.write_date'
        db.add_column(u'admin_sector', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Job.create_date'
        db.add_column(u'admin_job', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Job.write_date'
        db.add_column(u'admin_job', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Track.create_date'
        db.delete_column(u'admin_track', 'create_date')

        # Deleting field 'Track.write_date'
        db.delete_column(u'admin_track', 'write_date')

        # Deleting field 'Company.create_date'
        db.delete_column(u'admin_company', 'create_date')

        # Deleting field 'Company.write_date'
        db.delete_column(u'admin_company', 'write_date')

        # Deleting field 'Institution.create_date'
        db.delete_column(u'admin_institution', 'create_date')

        # Deleting field 'Institution.write_date'
        db.delete_column(u'admin_institution', 'write_date')

        # Deleting field 'SubSector.create_date'
        db.delete_column(u'admin_subsector', 'create_date')

        # Deleting field 'SubSector.write_date'
        db.delete_column(u'admin_subsector', 'write_date')

        # Deleting field 'Occupation.create_date'
        db.delete_column(u'admin_occupation', 'create_date')

        # Deleting field 'Occupation.write_date'
        db.delete_column(u'admin_occupation', 'write_date')

        # Deleting field 'Sector.create_date'
        db.delete_column(u'admin_sector', 'create_date')

        # Deleting field 'Sector.write_date'
        db.delete_column(u'admin_sector', 'write_date')

        # Deleting field 'Job.create_date'
        db.delete_column(u'admin_job', 'create_date')

        # Deleting field 'Job.write_date'
        db.delete_column(u'admin_job', 'write_date')


    models = {
        u'account.industryprofile': {
            'Meta': {'object_name': 'IndustryProfile'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['admin.Company']", 'null': 'True', 'blank': 'True'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'est_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_sector': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.UserProfile']", 'unique': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.company': {
            'Meta': {'object_name': 'Company'},
            'company_type': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'nasscom_membership_number': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '20'}),
            'training_provider': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '3'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '100'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.institution': {
            'Meta': {'object_name': 'Institution'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.City']", 'null': 'True', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'international': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_university': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'university_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '100'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.job': {
            'Meta': {'object_name': 'Job'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.IndustryProfile']"}),
            'is_internship': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_description': ('tinymce.models.HTMLField', [], {}),
            'job_role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.QualificationPack']"}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.State']"}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'admin.logentry': {
            'Meta': {'ordering': "(u'-action_time',)", 'object_name': 'LogEntry', 'db_table': "u'django_admin_log'"},
            'action_flag': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'change_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_repr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'admin.occupation': {
            'Meta': {'object_name': 'Occupation'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['admin.Track']", 'null': 'True', 'blank': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.occupationalstandard': {
            'Meta': {'unique_together': "(('code', 'version'),)", 'object_name': 'OccupationalStandard'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '9', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None'}),
            'drafted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'knowledge': ('tinymce.models.HTMLField', [], {'default': 'None'}),
            'last_reviewed_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'next_review_on': ('django.db.models.fields.DateField', [], {}),
            'performace_criteria': ('tinymce.models.HTMLField', [], {'default': 'None'}),
            'scope': ('tinymce.models.HTMLField', [], {'default': 'None'}),
            'skills': ('tinymce.models.HTMLField', [], {'default': 'None'}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '8', 'db_index': 'True'})
        },
        'admin.qualificationpack': {
            'Meta': {'object_name': 'QualificationPack'},
            'alias': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '9', 'blank': 'True'}),
            'drafted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'experience': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'job_role': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'db_index': 'True'}),
            'last_reviewed_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'max_educational_qualification': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'min_educational_qualification': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'next_jobs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['admin.QualificationPack']", 'null': 'True', 'blank': 'True'}),
            'next_review_on': ('django.db.models.fields.DateField', [], {}),
            'nveqf_level': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['admin.Occupation']"}),
            'os_compulsory': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'os_compulsory'", 'blank': 'True', 'to': "orm['admin.OccupationalStandard']"}),
            'os_optional': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'os_optional'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['admin.OccupationalStandard']"}),
            'role_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['admin.Track']", 'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '8', 'blank': 'True'})
        },
        'admin.sector': {
            'Meta': {'object_name': 'Sector', 'index_together': "[['name']]"},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '9', 'db_index': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.subsector': {
            'Meta': {'unique_together': "(('sector', 'name'),)", 'object_name': 'SubSector', 'index_together': "[['name', 'sector']]"},
            'career_guide': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobility_map': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'db_index': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Sector']"}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.track': {
            'Meta': {'object_name': 'Track'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'analytics.city': {
            'Meta': {'unique_together': "(('name', 'state'),)", 'object_name': 'City'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.State']"}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'analytics.state': {
            'Meta': {'unique_together': "(('name', 'region'),)", 'object_name': 'State'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
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
        }
    }

    complete_apps = ['admin']
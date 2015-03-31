# -*- coding: utf-8 -*-
"""
    account.models

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from admin.models import Company

__all__ = [
    'UserProfile', 'StudentProfile', 'IndustryProfile', 'TrainingProfile',
    'GovernmentProfile', 'IndustryProfileAdmin', 'TrainingProfileAdmin',
    'GovernmentProfileAdmin', 'StudentProfileAdmin',
]


class UserProfile(models.Model):
    """
    User Profile
    """
    ROLE_CHOICES = {
        ('S', 'Student / Job Seekers'),
        ('T', 'Training Providers'),
        ('I', 'Industry'),
        ('G', 'Government'),
    }
    user = models.OneToOneField(User)
    role = models.CharField(choices=ROLE_CHOICES, max_length=5)
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    def get_profile_model_form(self):
        """
        Return tuple of profile and profile form model based on role.
        """
        from account.forms import TrainingProfileForm, StudentProfileForm, \
            GovernmentProfileForm, IndustryProfileForm
        if self.role == "S":
            return (StudentProfile, StudentProfileForm)
        elif self.role == "T":
            return (TrainingProfile, TrainingProfileForm)
        elif self.role == "I":
            return (IndustryProfile, IndustryProfileForm)
        elif self.role == "G":
            return (GovernmentProfile, GovernmentProfileForm)

    def __unicode__(self):
        """
        Return object display name
        """
        return "%s - %s" % (self.get_role_display(), self.pk)


class StudentProfile(models.Model):
    """
    Student Profile
    """
    WORK_STATUS_CHOICES = {
        ('S', 'Studying'),
        ('E', 'Employed'),
        ('U', 'Unemployed'),
    }
    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    }
    EXPERIENCE_CHOICES = {
        ('F', 'Fresher'),
        ('1', '1 year'),
        ('2', '2 years'),
        ('5+', '5+ years'),
        ('15+', '15+ years'),
        ('25+', '25+ years'),
    }
    EDUCATION_CHOICES = {
        ('Not Pursuing Graduation', 'Not Pursuing Graduation'),
        ('B.A', 'B.A'),
        ('B.Arch', 'B.Arch'),
        ('BCA', 'BCA'),
        ('B.B.A', 'B.B.A'),
        ('B.Com', 'B.Com'),
        ('B.Ed', 'B.Ed'),
        ('BDS', 'BDS'),
        ('BHM', 'BHM'),
        ('B.Pharma', 'B.Pharma'),
        ('B.Sc', 'B.Sc'),
        ('B.Tech/B.E.', 'B.Tech/B.E.'),
        ('LLB', 'LLB'),
        ('MBBS', 'MBBS'),
        ('Diploma', 'Diploma'),
        ('BVSC', 'BVSC'),
        ('Other', 'Other'),
    }
    user_profile = models.OneToOneField(UserProfile)
    name = models.CharField(max_length=20)
    dob = models.DateField(null=True, verbose_name="Date of Birth")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2)
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    postal_code = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=12)
    telephone = models.CharField(max_length=12)
    educational_background = models.CharField(
        max_length=50, choices=EDUCATION_CHOICES
    )
    experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    key_skills = models.ManyToManyField(
        'admin.OccupationalStandard'
    )
    work_status = models.CharField(choices=WORK_STATUS_CHOICES, max_length=5)
    industry_belongs_to = models.CharField(
        max_length=50, blank=True, verbose_name="Industry"
    )
    functional_area = models.CharField(max_length=50, blank=True)
    current_company = models.CharField(
        max_length=50, blank=True, verbose_name="Current Company",
    )
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    def find_matching_jobs(self):
        """
        Returns jobs matching the key_skills of the person
        """
        from admin.models.qualification_pack import QualificationPack

        matching_jobs = []
        user_key_skills = set(self.key_skills.all())
        if not user_key_skills:
            return None
        for qp in QualificationPack.objects.filter(level__lt=30):
            qp_skills_compulsory = set(qp.os_compulsory.all())
            qp_skills_optional = set(qp.os_optional.all())

            # no of matching skills with 1.5 times weight
            match_index = len(qp_skills_compulsory & user_key_skills) * 1.5

            # add no of optional skills which match with 1
            match_index += len(qp_skills_optional & user_key_skills) * 1.0

            # Penalise for the skills you have but the job does not need
            match_index -= len(user_key_skills - qp_skills_compulsory) * .2
            match_index -= len(user_key_skills - qp_skills_optional) * .1

            matching_jobs.append({
                'qp': qp,
                'match_index': match_index,
                'matching_skills': len(qp_skills_compulsory & user_key_skills),
                'skill_gap': (qp_skills_compulsory - user_key_skills),
                'optional_skill_gap': (
                    qp_skills_optional - user_key_skills
                )
            })

        return sorted(
            matching_jobs, key=lambda job: job['match_index'],
            reverse=True
        )

    def __unicode__(self):
        """
        Return object display name
        """
        return self.name


class StudentProfileAdmin(admin.ModelAdmin):
    '''
    Industry profile view for admin
    '''
    list_display = ('__unicode__', 'gender', 'experience', 'work_status')


admin.site.register(StudentProfile, StudentProfileAdmin)


class IndustryProfile(models.Model):
    """
    Industry Profile
    """
    INDUSTRY_CHOICES = {
        ('IT', 'IT-ITes'),
        ('O', 'Other'),
    }
    user_profile = models.OneToOneField(UserProfile)
    name = models.CharField(max_length=100)
    est_year = models.IntegerField(
        null=True, verbose_name="Establishment Year (YYYY)"
    )
    industry_type = models.CharField(max_length=10, choices=INDUSTRY_CHOICES)
    sub_sector = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=12)
    company = models.ForeignKey(
        Company, default=None, null=True, blank=True
    )
    is_approved = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """
        Return object display name
        """
        return "%s, %s" % (self.name, self.contact_person)


class IndustryProfileAdmin(admin.ModelAdmin):
    '''
    Industry profile view for admin
    '''
    list_display = (
        '__unicode__', 'contact_person', 'email', 'is_approved',
    )


admin.site.register(IndustryProfile, IndustryProfileAdmin)


class TrainingProfile(models.Model):
    """
    Training Profile
    """
    TRAINER_CHOICES = {
        ('C', 'Company'),
        ('CC', 'Community College'),
        ('SG', 'State Government'),
        ('CG', 'Central Government'),
        ('TI', 'Training Institute'),
    }

    user_profile = models.OneToOneField(UserProfile)
    name = models.CharField(max_length=100)
    est_year = models.IntegerField(
        null=True, verbose_name="Establishment Year (YYYY)"
    )
    area_of_specialization = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=12)
    trainer_type = models.CharField(
        max_length=2, choices=TRAINER_CHOICES
    )
    is_approved = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """
        Return object display name
        """
        return self.name


class TrainingProfileAdmin(admin.ModelAdmin):
    '''
    Industry profile view for admin
    '''
    list_display = (
        '__unicode__', 'area_of_specialization', 'contact_person', 'email',
        'is_approved',
    )


admin.site.register(TrainingProfile, TrainingProfileAdmin)


class GovernmentProfile(models.Model):
    """
    Government Profile
    """
    DEPARTMENT_TYPES = {
        ('S', 'State'),
        ('C', 'Central'),
    }
    user_profile = models.OneToOneField(UserProfile)
    department = models.CharField(max_length=100)
    department_type = models.CharField(max_length=5, choices=DEPARTMENT_TYPES)
    region = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=12)
    is_approved = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """
        Return object display name
        """
        return self.department


class GovernmentProfileAdmin(admin.ModelAdmin):
    '''
    Government profile view for admin
    '''
    list_display = (
        '__unicode__', 'department_type',
        'contact_person', 'email', 'is_approved',
    )


admin.site.register(GovernmentProfile, GovernmentProfileAdmin)

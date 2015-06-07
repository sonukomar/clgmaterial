from django.db import models

# Create your models here.

class colleges(models.Model):
    ''' It stores the details of all the colleges '''     

    college_name = models.CharField(max_length = 300)
    University   = models.CharField(max_length = 300)
    state        = models.CharField(max_length = 300)
    city         = models.CharField(max_length = 300)

    def __unicode__(self):
        return unicode(self.college_name)


class branches(models.Model):
    ''' It Stores all the branch '''
    
    branch_name = models.CharField(max_length = 300)

    def __unicode__(self):
        return unicode(self.branch_name)



class subjects(models.Model):
    ''' It stores all the details of the available subjects '''

    subject_name = models.CharField(max_length = 300)
    branch       = models.ForeignKey('branches')   
    
    def __unicode__(self):
        return unicode(self.subject_name)


class chapters(models.Model):
        ''' It stores details of all the chapters corresponding to particular subjects '''

        chapter_name = models.CharField(max_length = 300)
        subject      = models.ForeignKey('subjects')

        def __unicode__(self):
                return unicode(self.chapter_name)

class notes_details(models.Model):
    ''' It stores the details of available notes with the us '''

    college = models.ForeignKey('colleges')
    branch  = models.ForeignKey('branches')
    subject = models.ForeignKey('subjects')               
    chapter = models.ForeignKey('chapters')
    pdf_id  = models.CharField(max_length = 300)

    def __unicode__(self):
        return unicode(self.chapter) 



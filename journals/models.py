from django.db import models

class Journal(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
        
    # Sortable | Visible in Listings View | Visible in Edit View
    journal_id = models.AutoField(primary_key=True)  

    # Sortable | Visible in Listings View | Visible in Edit View | Visible in Create View | Searchable
    journal_title = models.CharField(max_length=200)  

    # Sortable | Visible in Listings View | Visible in Edit View | Visible in Create View
    issn_print = models.CharField(max_length=20, blank=True, null=True)
    
    # Sortable | Visible in Listings View | Visible in Edit View | Visible in Create View
    issn_online = models.CharField(max_length=20, blank=True, null=True)

    # Sortable | Visible in Listings View | Visible in Edit View | Visible in Create View
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Inactive')

    # Visible in Edit View | Visible in Create View
    publisher = models.CharField(max_length=100, blank=True, null=True)

    # Visible in Edit View | Visible in Create View
    founder = models.CharField(max_length=100, blank=True, null=True)
    
    # Visible in Edit View | Visible in Create View
    issued_since_month = models.CharField(max_length=20, blank=True, null=True)

    # Visible in Edit View | Visible in Create View
    issued_since_year = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.journal_title


#Journal ID     #Sortable #Visible in Listings View #Visible in Edit View 
#Journal Title  #Sortable #Visible in Listings View #Visible in Edit View #Visible in Create View #Searchable
#ISSN (Print)   #Sortable #Visible in Listings View #Visible in Edit View #Visible in Create View
#ISSN (Online)  #Sortable #Visible in Listings View #Visible in Edit View #Visible in Create View
#Status         #Sortable #Visible in Listings View #Visible in Edit View #Visible in Create View
#Publisher*     #Visible in Edit View #Visible in Create View
#Founder*       #Visible in Edit View #Visible in Create View
#Issued Since month*       #Visible in Edit View #Visible in Create View
#Issued Since Year*        #Visible in Edit View #Visible in Create View


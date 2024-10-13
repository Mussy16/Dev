from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

      
class Posts(models.Model):
    ACTIVE = 'active'
    DRAFT ='draft'

    CHOICES_STATUS = [
       (ACTIVE,'Active'),
       (DRAFT,'Draft')
    ]
    category = models.ForeignKey(Category,related_name='posts',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=CHOICES_STATUS,default=ACTIVE)
    image = models.ImageField(upload_to='upload/',blank=True,null=True)

class Meta:
   ordering = ('-created_at',)

def __str__(self):
    return self.title

class Comment(models.Model):
    post = models.ForeignKey(Posts,related_name='comments',on_delete=models.CASCADE)
    mame = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mame
    
    #Here
class ArtifactReflection(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    infor = models.CharField(max_length=200)
    welcome  = models.TextField()
    image = models.ImageField(upload_to='artifact_images/')
    article_content = models.TextField()  # Field for detailed article content
    additional_image = models.ImageField(upload_to='artifacts/', blank=True, null=True)  # Optional additional image
    article_content2 = models.TextField() 
    video_url = models.URLField(blank=True, null=True)
    second = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)
    
    

    def __str__(self):
        return self.heading


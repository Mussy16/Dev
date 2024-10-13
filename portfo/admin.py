from django.contrib import admin

# Register your models here.
from .models import Posts,Category,Comment,ArtifactReflection

class CommentInlineIterm(admin.TabularInline):
     model = Comment
     raw_id_fields =  ['post']
     
class PostAdmin(admin.ModelAdmin):
     search_fields = ('title','intro','body')
     list_display = ('title','slug','category','created_at','status')
     list_filter =('category','created_at','status')
     inlines = [CommentInlineIterm]
     

class CategoryAdmn(admin.ModelAdmin):
      search_fields = ('title')
      list_display = ('title')
      prepopulated_fields = {'slug':['title,']}

class CommentAdmin(admin.ModelAdmin):
     list_display = ('name','post','created_at')

admin.site.register(Comment,)
admin.site.register(Posts,PostAdmin,)
@admin.register(Category,)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

class ArtifactsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description','image','article_content', 'additional_image','video_url','second','intro','article_content2')

admin.site.register(ArtifactReflection,ArtifactsAdmin)


from django.contrib import admin
from blogging.models import Post, Category

# and a new admin registration

class PostInline(admin.TabularInline):
    model = Category.posts.through
    


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
    inlines = [
        PostInline,
    ]

    
class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]   
    
    
#admin.site.register(PostInline)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
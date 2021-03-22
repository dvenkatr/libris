from django.contrib import admin
from book.models import Author, Award, Book, Review, Tag

admin.site.register(Author)
admin.site.register(Award)
# admin.site.register(Book)
# admin.site.register(Review)
admin.site.register(Tag)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'blurb', 'display_tag')
    fieldsets = (
        (None, {
            'fields': ['title']
        }),
        ('Meta', {
            'fields': ('isbn', 'pages', 'blurb')
        }),
    )


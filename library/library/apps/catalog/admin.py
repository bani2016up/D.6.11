from django.contrib import admin
from .models import Author, Book, PublishingHouse, Friend, BookInUse

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # @staticmethod
    # def author_full_name(obj):
    #     return obj.author.full_name
    list_display = ('title', 'author')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'ph_name', 'pic')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mail', 'address')
    fields = ('first_name', 'last_name', 'mail', 'address')

@admin.register(BookInUse)
class BookInUseAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'user_id', 'start_use_date', 'pic')
    fields = ('book_title', 'user_id', 'start_use_date', 'pic')
from django.contrib import admin

# Register your models here.
from . models import Tipo, Formato, Comic, Autor, ComicInstance

admin.site.register(Tipo)
admin.site.register(Formato)
admin.site.register(Comic)
admin.site.register(Autor)
admin.site.register(ComicInstance)
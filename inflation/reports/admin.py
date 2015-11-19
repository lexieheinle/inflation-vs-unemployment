from django.contrib import admin
from .models import Inflation
from .models import Unemployment
from .models import Interest
# Register your models here.
admin.site.register(Inflation)
admin.site.register(Unemployment)
admin.site.register(Interest)
from .models import Serviciu
from django.contrib import admin
from .models import Clienta
from .models import Programare
admin.site.register(Serviciu)

admin.site.register(Clienta)
admin.site.register(Programare)
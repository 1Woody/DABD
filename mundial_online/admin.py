from django.contrib import admin
from .models import Fabricant 
from .models import TeamPrincipal 
from .models import Pilot 
from .models import GranPremi 
from .models import Temporada 
from .models import MundialPilot 
from .models import MundialFabricant 
from .models import Resultat

admin.site.register(Fabricant)
admin.site.register(TeamPrincipal)
admin.site.register(Pilot)
admin.site.register(GranPremi)
admin.site.register(Temporada)
admin.site.register(MundialPilot)
admin.site.register(MundialFabricant)
admin.site.register(Resultat)
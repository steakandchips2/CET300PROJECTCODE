# import the path from url's and views froom this directory
from django.urls import path
from . import views


#create the url paths to redirect the user to the correct pages, organised by region, and subcategory.
urlpatterns = [
#main files
path("index", views.index, name="index"),
path("", views.home, name="home"),
path("home", views.home, name="home"),
path("about", views.about, name="about"),
path("globalgenre", views.globalgenre, name="globalgenre"),

#global urls
path("rms", views.rms, name="rms"),
path("globalgenre", views.globalgenre, name="globalgenre"),
path("globalplatform", views.globalplatform, name="globalplatform"),
path("globaltopgames", views.globaltg, name="globaltopgames"),

#europe urls
path("EUAllTime", views.euat, name="euat"),
path("eugenre", views.eugenre, name="eugenre"),
path("euplatform", views.euplatform, name="euplatform"),

#japan
path("jpatg", views.jpatg, name="jpatg"),
path("jpgenre", views.jpgenre, name="jpgenre"),
path("jpplatform", views.jpplatform, name="jpplatform"),

# USA
path("usatg", views.usatg, name="usatg"),
path("usgenre", views.usgenre, name="usgenre"),
path("usplatform", views.usplatform, name="usplatform"),

#other
path("otatg", views.otatg, name="otatg"),
path("otgenre", views.otgenre, name="otgenre"),
path("otplatform", views.otplatform, name="otplatform"),
]
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import subprocess
from scripts import *

#USE THIS TO CREATE THE 'VIEW' THIS IS HOW THE PYTHON FILES ARE RAN AND ALSO HOW OTHER PAGES ARE RENDERED.

def index(response, id):
    return render(response, "datavis/base.html", {})

def home(response):
    return render(response, "datavis/main/home.html", {})

def about(response):
    return render(response, "datavis/main/about.html", {})

# REGIONAL MARKETSHARE GRAPH, RENDERED IN REAL TIME. IF ANYTHING IN THE CSV IS CHANGED
# THEN THE GRAPHS WILL AUTOMATICALLY UPDATE BASED ON THAT. THE PYTHON FILE IS RAN EVERY TIME THE PAGE IS OPENED
### TESTING MULTIPLE ON ONE PAGE ####


#global genre - 7 graphs


#define the function that runs scripts.
def run_scripts_Global_Genre():
#get all of the scripts for the page 
    global_genre_scritps = ['GlobalGenre2010', 'GlobalGenre2011', 'GlobalGenre2012', 'GlobalGenre2013',
    'GlobalGenre2014', 'GlobalGenre2015', 'GlobalGenre2016']
    #loop trhough the scripts
    for global_genre_scritps in global_genre_scritps:
 #run and get the scripts from script name variable.
        subprocess.run(['python', f'scripts/{global_genre_scritps}.py'])
        
def globalgenre(request):
    #call global genre function
    run_scripts_Global_Genre() 
    #message for the user
    output = "Scripts executed successfully!"
    # pass to html
    context = {'plot_json': output}
    #render the html template
    return render(request, 'datavis/global/globalgenre.html', context)

#####
#global platform - 7 graphs
#define the function that runs scripts.
def run_scripts_Global_Platform():
    global_platform_scripts = ['GlobalPlatform2010', 'GlobalPlatform2011',
    'GlobalPlatform2012', 'GlobalPlatform2013', 'GlobalPlatform2014', 'GlobalPlatform2015', 'GlobalPlatform2016']
    for global_platform_scripts in global_platform_scripts:
        subprocess.run(['python', f'scripts/{global_platform_scripts}.py'])

def globalplatform(request):
    #call the function
    run_scripts_Global_Platform()
    #a message for the user
    output = "Scripts executed successfully!"
    # pass to html
    context = {'plot_json': output}
    #render the html template
    return render(request, 'datavis/global/globalplatform.html', context)
#####

#global top games 7 graphs

#define the function that runs scripts.
def run_scripts_Global_Top_Game():
    glob_top_script = ['Top_Game_2010', 'Top_Game_2011', 'Top_Game_2012', 'Top_Game_2013',
    'Top_Game_2014', 'Top_Game_2015', 'Top_Game_2016']
    for glob_top_script in glob_top_script:
        subprocess.run(['python', f'scripts/{glob_top_script}.py'])

def globaltg(request):
    #call the function
    run_scripts_Global_Top_Game()
#a message for the user
    output = "success!"
# pass to html
    context = {'plot_json': output}
#render the html template
    return render(request, 'datavis/global/globaltopgames.html', context)


## regional marketshare - 1 graph

#define the function that runs scripts.
def rms(request):
    # Run the rms.py script and get its output
    output = subprocess.check_output(['python', 'scripts/rms.py'])
    # Pass the output to the template
    context = {'plot_json': output}
    return render(request, 'datavis/global/rms.html', context)

    # Europe
#EUROPE ALL TIME GENRE SALES
    
def euat(request):
    # Run the eu all time script and get its output
    outputeuat = subprocess.check_output(['python', 'scripts/EUAllTimeGenre.py'])
    # Pass the output to the template
    contexteuat = {'plot_json': outputeuat}
    return render(request, 'datavis/europe/EUAllTime.html', contexteuat)

#define the function that runs scripts.
def run_scripts_EU_Genre():
    europe_genre_scripts = ['EUgenre2010', 'EUgenre2011',
    'EUgenre2012', 'EUgenre2013', 'EUgenre2014', 'EUgenre2015', 'EUgenre2016']
    for europe_genre_scripts in europe_genre_scripts:
        subprocess.run(['python', f'scripts/{europe_genre_scripts}.py'])

def eugenre(request):
    #call the function
    run_scripts_EU_Genre()
#a message for the user
    output = "Success!"
# pass to html
    context = {'plot_json': output}
#render the html template
    return render(request, 'datavis/europe/eugenre.html', context)

#define the function that runs scripts.
def run_scripts_EU_Platform():
    EU_plat_script = ['EUplat2010', 'EUplat2011', 'EUplat2012',
    'EUplat2013', 'EUplat2014', 'EUplat2015', 'EUplat2016']
    for EU_plat_script in EU_plat_script:
        subprocess.run(['python', f'scripts/{EU_plat_script}.py'])

#define the function that runs scripts.
def euplatform(request):
    #call the function
    run_scripts_EU_Platform()
#a message for the user
    output = "Scripts executed successfully!"
# pass to html
    context = {'plot_json': output}
#render the html template
    return render(request, 'datavis/europe/euplatform.html', context)

# JAPAN 
###fine
def jpatg(request):
    # Run the rms.py script and get its output
    outputjpatg = subprocess.check_output(['python', 'scripts/JPAllTimeGenre.py'])
    # Pass the output to the template
    contextjpatg = {'plot_json': outputjpatg}
    return render(request, 'datavis/japan/jpatg.html', contextjpatg)


####
#define the function that runs scripts.
def run_scripts_JP_Genre():
    JP_Genre_script = ['JPGenre2010', 'JPGenre2011', 'JPGenre2012', 'JPGenre2013',
    'JPGenre2014', 'JPGenre2015', 'JPGenre2016']
    for JP_Genre_script in JP_Genre_script:
        subprocess.run(['python', f'scripts/{JP_Genre_script}.py'])

def jpgenre(request):
    #call the function
    run_scripts_JP_Genre()
#a message for the user
    output = "Scripts executed successfully!"
# pass to html
    context = {'plot_json': output}
#render the html template
    return render(request, 'datavis/japan/jpgenre.html', context)


###


#define the function that runs scripts.
def run_scripts_JP_Platform():
    jp_plat_script = ['JPplatform2010', 'JPplatform2011', 'JPplatform2012', 'JPplatform2013',
    'JPplatform2014', 'JPplatform2015', 'JPplatform2016']
    for jp_plat_script in jp_plat_script:
        subprocess.run(['python', f'scripts/{jp_plat_script}.py'])

def jpplatform(request):
    #call the function
    run_scripts_JP_Platform()
#a message for the user
    output = "Scripts executed successfully!"
# pass to html
    context = {'plot_json': output}
#render the html template
    return render(request, 'datavis/japan/jpplatform.html', context)


### USA 


def usatg(request):
    # Run the rms.py script and get its output
    outputusatg = subprocess.check_output(['python', 'scripts/USAAllTimeGenre.py'])
    # Pass the output to the template
    contextusatg = {'plot_json': outputusatg}
    return render(request, 'datavis/usa/usatg.html', contextusatg)


    ####
#define the function that runs scripts.
def run_scripts_US_Genre():
    US_genre_script = ['USAGenre2010', 'USAGenre2011', 'USAGenre2012',
    'USAGenre2013', 'USAGenre2014', 'USAGenre2015', 'USAGenre2016']
    for US_genre_script in US_genre_script:
        subprocess.run(['python', f'scripts/{US_genre_script}.py'])

def usgenre(request):
    #call the function
    run_scripts_US_Genre()
#a message for the user
    output = "Scripts executed successfully!"
# pass to html
    context = {'plot_json': output}
#render the html template
    return render(request, 'datavis/usa/usgenre.html', context)

    ####
#define the function that runs scripts.
def run_scripts_US_Platform():
    US_Plat_script = ['USAplatform2010', 'USAplatform2011', 'USAplatform2012', 'USAplatform2013',
    'USAplatform2014', 'USAplatform2015', 'USAplatform2016']
    for US_Plat_script in US_Plat_script:
        subprocess.run(['python', f'scripts/{US_Plat_script}.py'])

def usplatform(request):
    #call the function
    run_scripts_US_Platform()
#a message for the user
    output = "Scripts executed successfully!"
# pass to html
    context = {'plot_json': output}
#render the html template
    return render(request, 'datavis/usa/usplatform.html', context)
#####

### other regions
def otatg(request):
    # Run the rms.py script and get its output
    outputotatg = subprocess.check_output(['python', 'scripts/OTAllTimeGenre.py'])
    # Pass the output to the template
    contextotatg = {'plot_json': outputotatg}
    return render(request, 'datavis/other/otatg.html', contextotatg)

####

#define the function that runs scripts.
def run_scripts_OT_Genre():
    OT_Genre_script = ['OTGenre2010', 'OTGenre2011', 'OTGenre2012',
    'OTGenre2013', 'OTGenre2014', 'OTGenre2015', 'OTGenre2016']
    for OT_Genre_script in OT_Genre_script:
        subprocess.run(['python', f'scripts/{OT_Genre_script}.py'])

def otgenre(request):
    #call the function
    run_scripts_OT_Genre()
#a message for the user
    output = "Scripts executed successfully!"
# pass to html
    context = {'plot_json': output}
#render the html template
    return render(request, 'datavis/other/otgenre.html', context)

####
#define the function that runs scripts.
def run_scripts_OT_Platform():
    OT_platform_script = ['OTPlatform2010', 'OTPlatform2011', 'OTPlatform2012', 'OTPlatform2013',
    'OTPlatform2014', 'OTPlatform2015', 'OTPlatform2016']
    for OT_platform_script in OT_platform_script:
        subprocess.run(['python', f'scripts/{OT_platform_script}.py'])

def otplatform(request):
    #call the function
    run_scripts_OT_Platform()
#a message for the user
    output = "Scripts executed successfully!"
# pass to html
    context = {'plot_json': output}
#render the html template
    return render(request, 'datavis/other/otplatform.html', context)
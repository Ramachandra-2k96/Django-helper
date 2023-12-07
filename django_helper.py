import os
import shutil

def create_django_project(project_name,app_name):
    try :
        # Step 1: Create a new Django project
        os.system(f"django-admin startproject {project_name}")
        # Step 2: Move inside project directory
        os.chdir(project_name)
        # Step 3: Create a Django app
        os.system(f"python manage.py startapp {app_name}")
    except Exception as e:
        if os.path.exists(project_name):
            shutil.rmtree(project_name)
        print(f"Error : {e}")
    
    setup_template(project_name,app_name)
    setup_setting(project_name,app_name)
    make_view(project_name,app_name)
    setup_urls(project_name,app_name)
    runserver()
    print(f"Django project '{project_name}' created successfully.")


def setup_template(project_name,app_name):
    # Step 4: Create a templates directory
    os.makedirs("templates")
    # Step 5: Create an HTML file inside the templates directory
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.16/dist/tailwind.min.css" rel="stylesheet">
        <title>Django Project</title>
    </head>
    <body class="bg-gray-100 font-sans">

        <div class="container mx-auto p-4">
            <header class="text-center mb-8">
                <h1 class="text-4xl font-bold text-blue-700">Django Project</h1>
            </header>

            <main class="text-center">
                <p class="text-lg text-gray-800">
                    This Django project named <span class="font-semibold text-blue-700">{project_name}</span> 
                    with the app <span class="font-semibold text-blue-700">{app_name}</span> has been created successfully.
                </p>
                <p class="text-md text-gray-600 mt-4">
                    This is just a demo content. Happy Coding!
                </p>
            </main>
        </div>

    </body>
    </html>
    """
    with open(os.path.join("templates", "index.html"), "w") as html_file:
        html_file.write(html)
        
        
def make_view(project_name,app_name):
    # Update/create views.py and write a method to run
    with open(os.path.join(app_name, "views.py"), "a") as file:
        file.write("\ndef home(request):\n\treturn render(request,'index.html')")


def setup_setting(project_name,app_name):
    # Step 6: Update Django settings to include the app and templates
    with open(os.path.join(project_name, "settings.py"), "a") as file:
        # Make it easy for hosting
        file.write(f"\nALLOWED_HOSTS.append('*')\n")
        file.write(f"\nimport os\n")
        #add installed apps
        file.write(f"\nINSTALLED_APPS += ['{app_name}',]\n")
        #
        file.write(f"TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR,'templates'),]\n")
 
 
def setup_urls(project_name,app_name):  
    with open(os.path.join(project_name, "urls.py"), "a") as file:
        file.write(f"\nfrom {app_name}.views import home\nurlpatterns.append(path('',home))")
        
     
def runserver():
    print("Staring server for you ......")
    print("Next steps are below")     
    print("1.views.py-Create your logic here and pass the result as param1 to index.html")
    print("2.index.html-Display result within {{param1}}")
    os.system(f"python manage.py runserver")
  
        
if __name__ == "__main__":
    project_name = input("Enter Django project name: ")
    if os.path.exists(project_name):
        print("project exists please try with different names ")
    else:
        try:
            import django
        except:
            os.system("pip install django")
        app_name = input("Enter Django App name: ")
        create_django_project(project_name,app_name)

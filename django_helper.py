import os
import shutil
import subprocess
import platform
import sys

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'
BOLD = '\033[1m'
ARROW_DOWN = '↓'
MAGENTA="\033[35m"
CYAN="\033[36m"
BG_WHITE = '\033[47m'
code_by = "Project by"

Name = """
 ██████╗  ██████╗  ███████╗   ███████╗ 
██╔════╝ ██╔═══██╗ ██╔═══██║  ██╔═══╝ 
██║	 ██║   ██║ ██║ 	  ██║ ███████╗ 
██║	 ██║   ██║ ██║   ██║  ██╔════╝
╚██████╗ ╚██████╔╝ ╚██████╔╝  ███████╗ 
 ╚═════╝  ╚═════╝   ╚═════╝   ╚══════╝ 
  ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗████████╗ ██╗   ██╗███╗   ███╗ 
██╔═══██╗ ██║   ██║██╔══██╗████╗  ██║╚══██╔══╝ ██║   ██║████╗ ████║
██║   ██║ ██║   ██║███████║██╔██╗ ██║   ██║    ██║   ██║██╔████╔██║
██║▄▄ ██║ ██║   ██║██╔══██║██║╚██╗██║   ██║    ██║   ██║██║╚██╔╝██║
╚██████╔╝ ╚██████╔╝██║  ██║██║ ╚████║   ██║    ╚██████╔╝██║ ╚═╝ ██║
 ╚══▀▀═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝     ╚═════╝ ╚═╝     ╚═╝
"""

class Normal_Use_Functions:
    # Function to print "code by" message with smaller font size
    def print_code_by(self):
        # Print "code by" message with reduced spacing between characters
        print("\n"+f"{BOLD}{GREEN}"+" ".join(letter for letter in code_by))
        print(Name)
        
    def run_command(self, command):
        """Run a shell command and print output."""
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in process.stdout:
            print(line.decode(), end='')
        for line in process.stderr:
            print(line.decode(), end='')
        process.wait()
        
    def run_command_in_env(self,python_bin,command):
        """Run a shell command and print output."""
        full_command = f"{python_bin} -m {command}"
        process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in process.stdout:
            print(line.decode(), end='')
        for line in process.stderr:
            print(line.decode(), end='')
        process.wait()
        
    def is_virtualenv(self):
        """Check if the script is running inside a virtual environment."""
        return (
            hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) or
            os.getenv('VIRTUAL_ENV') is not None
        )  
    
    def create_virtualenv(self, venv_name = "venv"):
        """Create a virtual environment."""
        self.run_command(f"python3 -m venv {venv_name}")
        
    def platform_script(self, venv_name ="venv"):
        """Return the activation script command based on the platform."""
        if platform.system() == "Windows":
            python_bin = os.path.join(venv_name, 'Scripts', 'python.exe')
        else:
            python_bin = os.path.join(venv_name, 'bin', 'python')
        return python_bin
        
    def install_dependecy(self, python_path,dependecy="django"):
        """Install Django in the virtual environment."""
        self.run_command_in_env(python_bin=python_path,command="pip install --upgrade pip")
        self.run_command_in_env(python_bin=python_path,command=f"pip install {dependecy}")
        
    def generate_requirements(self, python_path,file_name = "requirements.txt"):
        """Generate a requirements.txt file with the installed packages."""
        self.run_command_in_env(python_bin=python_path,command=f"pip freeze > {file_name}")
    
class normal_Django(Normal_Use_Functions):
    #Code Quantum
    def create_django_project(self,project_name,app_name):
        try :
            os.makedirs(project_name, exist_ok=True)
            os.chdir(project_name)
            self.create_virtualenv()
            python_bin = self.platform_script()
            """ Install All dependency's"""    
            self.install_dependecy(python_path=python_bin,dependecy="django")       
            os.system(f"django-admin startproject {project_name}")
            self.create_Django_App(project_name,app_name)
            os.chdir(os.path.dirname(os.getcwd()))
            self.generate_requirements(python_path=python_bin)
        except Exception as e:
            print(f"{BOLD}{RED}Error : {e}!{RESET}")
            
    def create_Django_App(self,project_name,app_name):
        try :
            # Step 1: Move to Django Project
            os.chdir(project_name)
            # Step 2: Create a Django app
            os.system(f"django-admin startapp {app_name}") 
            self.setup_template(project_name,app_name)
            self.setup_setting(project_name,app_name)
            self.make_view(project_name,app_name)
            self.setup_urls(project_name,app_name)
            print(f"{BOLD}{GREEN}Django project '{project_name}' created successfully.{RESET}")
        except Exception as e:
            if os.path.exists(project_name):
                shutil.rmtree(project_name)
            print(f"{BOLD}{RED}Error : {e}!{RESET}")

    def setup_template(self,project_name,app_name):
        # Step 4: Create a templates directory
        os.chdir(app_name)
        os.makedirs(f"templates/{app_name}")
        os.makedirs(f"static/{app_name}/js")
        os.makedirs(f"static/{app_name}/css")
        # Step 5: Create an HTML file inside the templates directory
        html = f"""
    {{% load static %}}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Django Project</title>
        <link rel="stylesheet" href="{{% static '{app_name}/css/style.css' %}}">
    </head>
    <body>
        <header>
            <h1>Django Project</h1>
        </header>
        <nav class="navbar" id="myNavbar">
            <a href="#" class="icon" onclick="toggleMenu()">&#9776;</a>
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
        </nav>
        <main>
            <section>
                <div class="container">
                    <h1>Congratulations!</h1>
                    <p>Your Django project, named <strong>{project_name}</strong> with the app <strong>{app_name}</strong>, has been successfully created.</p>
                    <p>This is just a demo content. Happy Coding!</p>
                    <a href="#" class="button">Get Started</a>
                </div>
            </section>
        </main>
        <footer>
            <div class="container">
                <p>&copy; 2024 Django Project. All rights reserved.</p>
            </div>
        </footer>
        <script src="{{% static '{app_name}/js/script.js' %}}" defer></script>
    </body>
    </html>
    """

        js="""
                // Toggle responsive navigation menu
            function toggleMenu() {
                var x = document.getElementById("myNavbar");
                if (x.className === "navbar") {
                    x.className += " responsive";
                } else {
                    x.className = "navbar";
                }
            }

            // Smooth scrolling
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();

                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
        """
        css=""" 
            body {
                    font-family: 'Roboto', sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f8f9fa;
                    color: #333;
                }
            header {
                background-color: #007bff;
                color: #fff;
                padding: 20px 0;
                text-align: center;
            }
            main {
                padding: 50px 0;
                text-align: center;
            }
            section{
                height: 60vh;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
            .button {
                display: inline-block;
                background-color: #007bff;
                color: #fff;
                padding: 10px 20px;
                border-radius: 5px;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }
            .button:hover {
                background-color: #0056b3;
            }
            footer {
                background-color: #333;
                color: #fff;
                padding: 20px 0;
                text-align: center;
            }

            .navbar {
                overflow: hidden;
                background-color: #007bff;
            }
            .navbar a {
                float: left;
                display: block;
                color: #fff;
                text-align: center;
                padding: 14px 20px;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }
            .navbar a:hover {
                background-color: #0056b3;
            }
            .navbar .icon {
                display: none;
            }

            @media screen and (max-width: 600px) {
                .navbar a:not(:first-child) {display: none;}
                .navbar a.icon {
                    float: right;
                    display: block;
                }
            }

            h1 {
                font-family: 'Montserrat', sans-serif;
                font-weight: 900;
                font-size: 3rem;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 20px;
                line-height: 1.6;
            }
        """
        with open(os.path.join(f"templates/{app_name}", "index.html"), "w") as html_file:
            html_file.write(html)
        with open(os.path.join(f"static/{app_name}/js", "script.js"), "w") as js_file:
            js_file.write(js)
        with open(os.path.join(f"static/{app_name}/css", "style.css"), "w") as css_file:
            css_file.write(css)
         
    def make_view(self,project_name,app_name):
        # Update/create views.py and write a method to run
        with open(os.path.join(app_name,"views.py"), "a") as file:
            file.write(f"def home(request):\n\treturn render(request,'{app_name}/index.html')")
        with open(os.path.join(app_name,"forms.py"), "w") as file:
            file.write(f"from django import forms\nclass inputform(forms.Form):\n\tinput=forms.CharField(label='Enter')\n")
        with open(os.path.join(app_name,"urls.py"), "w") as file:
            file.write(f"from django.urls import path\nfrom {app_name}.views import home\nurlpatterns = [\n\tpath('',home),\n]")

    def setup_setting(self,project_name,app_name):
        os.chdir(os.path.dirname(os.getcwd()))
        with open(os.path.join(project_name, "settings.py"), "r+") as file:
            content = file.read()
            modified_content = content.replace("ALLOWED_HOSTS = []",f"ALLOWED_HOSTS = ['*']")
            file.seek(0)
            file.write(modified_content)
            file.truncate()  # If the new content is shorter than the original, truncate the file
            with open(os.path.join(project_name, "settings.py"), 'r')as file:
                list1= file.readlines()
            index=0
            for j,i in enumerate(list1):
                if 'INSTALLED_APPS' in i:
                    index=j
                    break
            list1[index]=list1[index]+f"\t'{app_name}',\n"
            with open(os.path.join(project_name, "settings.py"), 'w')as file:
                file.writelines(list1)
 
    def setup_urls(self,project_name,app_name):  
        with open(os.path.join(project_name, "urls.py"), "r+") as file:
            content = file.read()
            if "from django.urls import path, include" not in content:
                modified_content = content.replace("from django.urls import path", "from django.urls import path, include")
                file.seek(0)
                file.write(modified_content)
            file.truncate()  # If the new content is shorter than the original, truncate the file
        with open(os.path.join(project_name, "urls.py"), 'r')as file:
            list= file.readlines()
        index=0
        for j,i in enumerate(list):
            if 'urlpatterns=[' in i.replace(" ", ""):
                index=j
                break
        list[index]=list[index]+f"\tpath('{app_name}/',include('{app_name}.urls')),\n"
        with open(os.path.join(project_name, "urls.py"), 'w')as file:
            file.writelines(list)
        print(f"{BOLD}{GREEN}Next steps are below {ARROW_DOWN}{RESET}")
        print(f"{BOLD}{GREEN}1.views.py-Create your logic here and pass the result as param1 to index.html{RESET}")
        print(f"{BOLD}{GREEN}2.index.html-Display result within {{param1}}{RESET}")
         
class Django_REST(Normal_Use_Functions):
    def create_django_project(self,project_name,app_name):
        try :
            os.makedirs(project_name, exist_ok=True)
            os.chdir(project_name)
            self.create_virtualenv()
            python_bin = self.platform_script()
            """ Install All dependency's"""    
            self.install_dependecy(python_path=python_bin,dependecy="django djangorestframework")       
            os.system(f"django-admin startproject {project_name}")
            os.chdir(project_name)
            # Step 2: Create a Django app
            os.system(f"django-admin startapp {app_name}")
            os.chdir(project_name)
            self.setup_setting(project_name,'rest_framework')
            self.setup_setting(project_name,app_name)
            self.setup_urls(project_name,app_name)
            
            self.setup_models(project_name,app_name)
            self.create_views(project_name,app_name)
            self.create_serializer(project_name,app_name)
            
            os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
            self.generate_requirements(python_path=python_bin)
            
        except Exception as e:
            print(f"{BOLD}{RED}Error : {e} !{RESET}")
            
    def setup_setting(self, project_name, app_name):
        with open("settings.py", "r+") as file:
            content = file.read()
            # Modify ALLOWED_HOSTS
            modified_content = content.replace("ALLOWED_HOSTS = []", "ALLOWED_HOSTS = ['*']")
            # Modify INSTALLED_APPS
            lines = modified_content.splitlines()
            for idx, line in enumerate(lines):
                if 'INSTALLED_APPS' in line:
                    # Insert the app name if not already in the list
                    if f"'{app_name}'" not in lines[idx + 1]:
                        lines[idx + 1] = lines[idx + 1].rstrip() + f"\n    '{app_name}',"
                    break
            # Write the changes back to the file
            file.seek(0)
            file.write("\n".join(lines))
            file.truncate()
 
    def setup_models(self, project_name, app_name):
        """entry directory /home/ramachandra/Desktop/Django-helper/r/r/r"""
        os.chdir(os.path.join(os.path.dirname(os.getcwd()),app_name))
        """ now /home/ramachandra/Desktop/Django-helper/r/r/a"""
        with open("models.py", "w") as file:
            content="""from django.db import models\n\nclass Item(models.Model):\n\tname = models.CharField(max_length=100)\n\tdescription = models.TextField()\n\tdef __str__(self):\n\t\treturn self.name"""
            file.write(content)
            
    def create_serializer(self, project_name, app_name):
        with open("serializers.py", "w") as file:
            content="""from rest_framework import serializers\nfrom .models import Item\n\nclass ItemSerializer(serializers.ModelSerializer):\n\tclass Meta:\n\t\tmodel = Item\n\t\tfields = '__all__'"""
            file.write(content)
    
    def create_views(self, project_name, app_name):
        with open("views.py", "w") as file:
            content="""from rest_framework import generics\nfrom .models import Item\nfrom .serializers import ItemSerializer\nclass ItemListCreate(generics.ListCreateAPIView):\n\tqueryset = Item.objects.all()\n\tserializer_class = ItemSerializer\nclass ItemDetail(generics.RetrieveUpdateDestroyAPIView):\n\tqueryset = Item.objects.all()\n\tserializer_class = ItemSerializer"""
            file.write(content)
        with open("urls.py", "w") as file:
            content="""from django.urls import path\nfrom .views import ItemListCreate, ItemDetail\nurlpatterns = [\n\tpath('items/', ItemListCreate.as_view(), name='item-list-create'),\n\tpath('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),\n]"""
            file.write(content)
        
    def setup_urls(self, project_name, app_name):
        with open("urls.py", "r+") as file:
            content = file.read()
            if "from django.urls import path, include" not in content:
                modified_content = content.replace("from django.urls import path", "from django.urls import path, include")
                file.seek(0)
                file.write(modified_content)
            file.truncate()  # If the new content is shorter than the original, truncate the file
        with open("urls.py", 'r')as file:
            list= file.readlines()
        index=0
        for j,i in enumerate(list):
            if 'urlpatterns=[' in i.replace(" ", ""):
                index=j
                break
        list[index]=list[index]+f"\tpath('{app_name}/',include('{app_name}.urls')),\n"
        with open("urls.py", 'w')as file:
            file.writelines(list)
        print(f"{BOLD}{GREEN}Next steps are below {ARROW_DOWN}{RESET}")
        print(f"{BOLD}{GREEN}1.views.py - Create your logic here and pass the result as param1 to index.html{RESET}")
        print(f"{BOLD}{GREEN}2. models and create serializer {RESET}")
        print(f"{BOLD}{GREEN}3. Run the below command {ARROW_DOWN} {RESET}")
        print(f"{BG_WHITE}{MAGENTA}python manage.py makemigrations{RESET}\n{BG_WHITE}{MAGENTA}python manage.py migrate{RESET}")
    
class Django_Websocket(Normal_Use_Functions):
    def create_Djnago_project(self, project_name, app_name):
        try :
            os.makedirs(project_name, exist_ok=True)
            os.chdir(project_name)
            self.create_virtualenv()
            python_bin = self.platform_script()
            """ Install All dependency's"""    
            self.install_dependecy(python_path=python_bin,dependecy="django channels daphne")       
            os.system(f"django-admin startproject {project_name}")
            os.chdir(project_name)
            # Step 2: Create a Django app
            os.system(f"django-admin startapp {app_name}")
            os.chdir(project_name)
            self.edit_settings(project_name,app_name)
            self.edit_asgi(project_name,app_name)
            self.configure_mainurl(project_name,app_name)
            
            """entry directory /home/ramachandra/Desktop/Django-helper/r/r/r"""
            os.chdir(os.path.join(os.path.dirname(os.getcwd()),app_name))
            """ now /home/ramachandra/Desktop/Django-helper/r/r/a"""
            
            self.create_consumers()
            self.create_routing()
            self.configure_appurl()
            self.configure_views(app_name)
            self.write_html(app_name)
            
            os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
            self.generate_requirements(python_path=python_bin)
            print(f"{BG_WHITE} Run : {GREEN} daphne -b 0.0.0.0 -p 8000 {project_name}.asgi:application{RESET}{BG_WHITE} in terminal to view ouput at {GREEN} http://127.0.0.1:8000/app/ {RESET}")
            
        except Exception as e:
            print(f"{BOLD}{RED}Error : {e} !{RESET}")
    
    def edit_settings(self, project_name, app_name):
        with open("settings.py", "r+") as file:
            content = file.read()
            # Modify ALLOWED_HOSTS
            modified_content = content.replace("ALLOWED_HOSTS = []", "ALLOWED_HOSTS = ['*']")
            # Modify INSTALLED_APPS
            modified_content = modified_content.replace(f"WSGI_APPLICATION = '{project_name}.wsgi.application'", f"ASGI_APPLICATION = '{project_name}.asgi.application'")
            lines = modified_content.splitlines()
            for idx, line in enumerate(lines):
                if 'INSTALLED_APPS' in line:
                    # Insert the app name if not already in the list
                    if f"'{app_name}'" not in lines[idx + 1]:
                        lines[idx + 1] = lines[idx + 1].rstrip() + f"\n\t'{app_name}',\n\t'channels',"
                    break
            # Write the changes back to the file
            file.seek(0)
            file.write("\n".join(lines))
            file.truncate()
        with open('settings.py','a') as file:
            content ="""CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
"""
            file.write("\n\n"+content)
    
    def edit_asgi(self, project_name, app_name):
        with open('asgi.py', 'w') as file:
            content = f"""import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from {app_name}.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')

application = ProtocolTypeRouter({{
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
}})
    """
            file.write(content)

    def configure_mainurl(self, project_name, app_name):
        with open("urls.py", "r+") as file:
            content = file.read()
            if "from django.urls import path, include" not in content:
                modified_content = content.replace("from django.urls import path", "from django.urls import path, include")
                file.seek(0)
                file.write(modified_content)
            file.truncate()  # If the new content is shorter than the original, truncate the file
        with open("urls.py", 'r')as file:
            list= file.readlines()
        index=0
        for j,i in enumerate(list):
            if 'urlpatterns=[' in i.replace(" ", ""):
                index=j
                break
        list[index]=list[index]+f"\tpath('{app_name}/',include('{app_name}.urls')),\n"
        with open("urls.py", 'w')as file:
            file.writelines(list)   
    
    def create_consumers(self):
        with open('consumers.py','w')as file:
            content = """import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Echo the received message back to WebSocket
        self.send(text_data=json.dumps({
            'message': "I recived : "+message
        }))
"""     
            file.write(content)

    def create_routing(self):
        with open('routing.py','w')as file:
            content = """from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
]
"""
            file.write(content)
        
    def configure_appurl(self):
        with open('urls.py','w')as file:
            content ="""from django.urls import path
from .views import home
urlpatterns = [
    path('',home)
]
"""
            file.write(content)
            
    def configure_views(self, app_name):
        with open('views.py','w')as file:
            content= f"""from django.shortcuts import render
def home(request):
    return render(request, '{app_name}/index.html')"""
            file.write(content)
    
    def write_html(self, app_name):
        os.makedirs(f'templates/{app_name}', exist_ok=True)
        with open(f'templates/{app_name}/index.html','w') as file:
            content ="""<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Example</title>
</head>
<body>
    <h1>WebSocket Test</h1>
    <textarea id="chat-log" cols="100" rows="20"></textarea><br>
    <input id="chat-message-input" type="text" size="100"><br>
    <button id="send-message">Send</button>

    <script>
        const chatSocket = new WebSocket(
            'ws://' + window.location.host + '/ws/chat/');

        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            document.querySelector('#chat-log').value += (data.message + '');
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

        document.querySelector('#send-message').onclick = function() {
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInputDom.value = '';
        };
    </script>
</body>
</html>
"""
            file.write(content)

def call_function(option:int)->int:
    match option:
        case 1:
                selected_option = 0
                normal = normal_Django()
                while True:
                    selected_option = int(input(f"{BOLD}{MAGENTA}\n\n1.Create new project \n2.Create App for existing project \n3.GO Back\n\nChoose an option: {RESET}"))
                    if not 0<selected_option<=3:
                        print(f"{BOLD}{BG_WHITE}{RED}\nInvalid option {RESET}")
                        pass
                    else:
                        break
                    
                if selected_option == 1:
                    project_name = input(f"{CYAN}Enter Django project name: ")
                    
                    if os.path.exists(project_name):
                        print(f"{BOLD}{RED}\nProject exists please try with different names {RESET}")    
                    else:
                        app_name = input(f"{CYAN}Enter new Django App name: ")
                        if os.path.exists(app_name):
                            print(f"{BOLD}{RED}\napp exists please try with different names {RESET}")    
                        else:
                            normal.create_django_project(project_name,app_name)
                            
                elif selected_option == 2:
                    project_name = input(f"{CYAN}Enter Django project name: ")
                    condition = os.path.exists(project_name)
                    project_dir=os.path.abspath(project_name)
                    all_files_and_dirs = os.listdir(project_dir)
                    
                    if condition and not ('manage.py' in all_files_and_dirs or project_name in all_files_and_dirs) :
                        print(f"{BOLD}{MAGENTA} I think you are inside the project direcotry so i am going one directory level up{RESET}")
                        os.chdir(os.path.dirname(os.path.dirname(project_dir)))
                        
                    while(condition):
                        app_name = input(f"{CYAN}Enter new Django App name: ")
                        while(os.path.exists(os.path.join(os.path.join(project_name,project_name),app_name))):
                            print(f"{BOLD}{RED}app exists please try with different names {RESET}")
                            app_name = input("Enter new Django App name: ")
                        os.chdir(project_name)
                        print(os.getcwd())
                        normal.create_Django_App(project_name,app_name)
                        break
                    else:
                        print(f"{BOLD}{RED}\nproject does not exists please try with different names {RESET}")    
                elif selected_option == 3:
                    return -1
                return 0
            
        case 2:
            rest = Django_REST()
            project_name = input(f"\n{CYAN}Enter Django-Rest project name: ")
            
            if os.path.exists(project_name):
                print(f"{BOLD}{RED}\nProject exists please try with different names {RESET}")    
            else:
                app_name = input(f"{CYAN}Enter new Django App name: ")
                if os.path.exists(app_name):
                    print(f"{BOLD}{RED}\napp exists please try with different names {RESET}")    
                else:
                    rest.create_django_project(project_name,app_name)
                    
            return 0
        
        case 3:
                socket = Django_Websocket()
                project_name = input(f"\n{CYAN}Enter Django-Web socket project name: ")
                
                if os.path.exists(project_name):
                    print(f"{BOLD}{RED}\nProject exists please try with different names {RESET}")    
                else:
                    app_name = input(f"{CYAN}Enter new Django App name: ")
                    if os.path.exists(app_name):
                        print(f"{BOLD}{RED}\napp exists please try with different names {RESET}")    
                    else:
                        socket.create_Djnago_project(project_name,app_name)
                        
                return 0
        case 4:
            return 0
        
        case _:
            print(f"{BOLD}{BG_WHITE}{RED}\nInvalid option{RESET}")
            return -1
        
if __name__ == "__main__": 
    normal = Normal_Use_Functions()
    normal.print_code_by()
    while True :
        selected_option = int(input(f"{BOLD}{MAGENTA}\n\n1.Django Project \n2.Django-REST Project \n3.Django-Web socket \n4.Exit\nChoose an option: {RESET}"))
        output = call_function(selected_option)
        if output == 0:
            break
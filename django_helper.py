import os
import shutil
RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'
BOLD = '\033[1m'
ARROW_DOWN = '↓'
MAGENTA="\033[35m"
CYAN="\033[36m"
code_by = "Code by"
Name = """
██████╗  ██╗ ███╗   ██  █████╗  ██████╗ ██╗   ██╗	
██╔══██╗ ██║ ████╗  ██║██╔══██╗	██╔══██╗╚██╗ ██╔╝	
██████╔╝ ██║ ██╔██╗ ██║███████║ ██████╔╝ ╚████╔╝ 	
██╔══██╗ ██║ ██║╚██╗██║██╔══██║ ██╔══██╗  ╚██╔╝  	
██████╔╝ ██║ ██║ ╚████║██║  ██║ ██║  ██║   ██║   	
╚═════╝  ╚═╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═╝  ╚═╝   ╚═╝   	
██╗    ██╗ ██╗   ██╗ ██╗███████╗██████╗ ███████╗  ██████╗ ███████╗██████╗ ███████╗
██║    ██║ ██║   ██║ ██║██╔════╝██╔══██╗██╔═══╝   ██╔══██╗██╔════╝██╔══██╗██╔════╝ 
██║ █╗ ██║ ████████║ ██║███████╗██████╝ ███████╗  ██████╔╝███████╗██████╔╝███████╗  
██║███╗██║ ██║   ██║ ██║╚════██║██╔══   ██╔════╝  ██╔══██╗██╔════╝██╔══██╗██╔════╝ 
╚███╔███╔╝ ██║   ██║ ██║███████║██╝ 	███████╗  ██║  ██║███████╗██║  ██║███████╗
 ╚══╝╚══╝  ╚═╝   ╚═╝ ╚═╝╚══════╝╚═╝  	╚══════╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ 
"""
# Function to print "code by" message with smaller font size
def print_code_by():
    # Print "code by" message with reduced spacing between characters
    print("\n"+f"{BOLD}{GREEN}"+" ".join(letter for letter in code_by))



def create_django_project(project_name,app_name):
    try :
        # Step 1: Create a new Django project
        os.system(f"django-admin startproject {project_name}")
        create_Django_App(project_name,app_name)
    except Exception as e:
        if os.path.exists(project_name):
            shutil.rmtree(project_name)
        print(f"{BOLD}{RED}Error : {e}!{RESET}")
        
def create_Django_App(project_name,app_name):
    try :
        # Step 1: Move to Django app
        os.chdir(project_name)
        # Step 2: Create a Django app
        os.system(f"django-admin startapp {app_name}") 
        setup_template(project_name,app_name)
        setup_setting(project_name,app_name)
        make_view(project_name,app_name)
        setup_urls(project_name,app_name)
        print(f"{BOLD}{GREEN}Django project '{project_name}' created successfully.{RESET}")
    except Exception as e:
        if os.path.exists(project_name):
            shutil.rmtree(project_name)
        print(f"{BOLD}{RED}Error : {e}!{RESET}")

def setup_template(project_name,app_name):
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
        
        
def make_view(project_name,app_name):
    # Update/create views.py and write a method to run
    with open(os.path.join(app_name,"views.py"), "a") as file:
        file.write(f"def home(request):\n\treturn render(request,'{app_name}/index.html')")
    with open(os.path.join(app_name,"forms.py"), "w") as file:
        file.write(f"from django import forms\nclass inputform(forms.Form):\n\tinput=forms.CharField(label='Enter')\n")
    with open(os.path.join(app_name,"urls.py"), "w") as file:
        file.write(f"from django.urls import path\nfrom {app_name}.views import home\nurlpatterns = [\n\tpath('',home),\n]")


def setup_setting(project_name,app_name):
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
 
def setup_urls(project_name,app_name):  
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
         
if __name__ == "__main__":
    print_code_by()
    print(Name)
    selected_option = input(f"{BOLD}{MAGENTA}Choose an option: \n1.Create new project \n2.Create App for existing project \n3.Exit\n{RESET}")
    if selected_option == "1":
        project_name = input(f"{CYAN}Enter Django project name: ")
        if os.path.exists(project_name):
            print(f"{BOLD}{RED}Project exists please try with different names {RESET}")    
        else:
            try:
                import django
            except:
                os.system("pip install django")
            app_name = input(f"{CYAN}Enter new Django App name: ")
            if os.path.exists(app_name):
                print(f"{BOLD}{RED}app exists please try with different names {RESET}")    
            else:
                create_django_project(project_name,app_name)
    elif selected_option == "2":
        project_name = input(f"{CYAN}Enter Django project name: ")
        condition = os.path.exists(project_name)
        project_dir=os.path.abspath(project_name)
        all_files_and_dirs = os.listdir(project_dir)
        if condition and not ('manage.py' in all_files_and_dirs or project_name in all_files_and_dirs) :
            print(f"{BOLD}{MAGENTA} I think you are inside the project direcotry so i am going one directory level up{RESET}")
            os.chdir(os.path.dirname(os.path.dirname(project_dir)))
            print(os.getcwd())
        while(condition):
            app_name = input(f"{CYAN}Enter new Django App name: ")
            while(os.path.exists(os.path.join(project_name,app_name))):
                print(f"{BOLD}{RED}app exists please try with different names {RESET}")
                app_name = input("Enter new Django App name: ")
            create_Django_App(project_name,app_name)
            break
        else:
            print(f"{BOLD}{RED}project does not exists please try with different names {RESET}")    
    else:
        print(f"{BOLD}{RED}Exiting")


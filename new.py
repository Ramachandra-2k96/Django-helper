import os
import sys
import subprocess

def run_command(command):
    """Run a shell command and print output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in process.stdout:
        print(line.decode(), end='')
    for line in process.stderr:
        print(line.decode(), end='')
    process.wait()

def create_virtualenv(venv_name):
    """Create a virtual environment."""
    run_command(f"python3 -m venv {venv_name}")

def activate_virtualenv(venv_name):
    """Activate the virtual environment."""
    activate_script = os.path.join(venv_name, 'bin', 'activate')
    return activate_script

def install_django():
    """Install Django in the virtual environment."""
    run_command("pip install --upgrade pip")
    run_command("pip install django")

def start_django_project(project_name):
    """Start a new Django project."""
    run_command(f"django-admin startproject {project_name} .")

def apply_migrations():
    """Run initial migrations."""
    run_command("python manage.py migrate")

def start_dev_server():
    """Start the Django development server."""
    run_command("python manage.py runserver")

if __name__ == "__main__":
    # Get the project name from the command line arguments
    if len(sys.argv) != 2:
        print("Usage: python setup_django.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]

    # Create a project directory
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    # Create and activate a virtual environment
    venv_name = "venv"
    create_virtualenv(venv_name)

    activate_script = activate_virtualenv(venv_name)
    print(f"To activate the virtual environment, run:\nsource {activate_script}")
    
    # Activate the virtual environment in the script
    subprocess.call(f"source {activate_script} && pip install --upgrade pip && pip install django", shell=True)

    # Install Django
    install_django()

    # Start a new Django project
    start_django_project(project_name)

    # Apply initial migrations
    apply_migrations()

    # Start the development server
    start_dev_server()

    print(f"Django project '{project_name}' has been created and the development server is running.")
    print("To deactivate the virtual environment, use the command 'deactivate'.")

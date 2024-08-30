# Django Helper  🚀

Django Helper is a tool to assist with Django project tasks. Follow the instructions below to get started.
By completing this procedure you will be able to use this utility on any terminal in your system. 

## 🛠️ Usage and Setup in 🪟 Windows

1. **Clone the Project:**
   - Navigate to the desired location and clone the Django Helper project:
     ```bash
     git clone https://github.com/Ramachandra-2k96/Django-helper.git
     ```

2. **Update the Batch File:**
   - Navigate to the cloned project directory and locate `django_helper.bat`.
   - Open `django_helper.bat` in a text editor.
   - Update the path to the Python script in the batch file:
     ```bat
     python C:\path\to\your\django_helper.py
     ```
     Replace `C:\path\to\your\` with the actual path to `django_helper.py` in the cloned project.

3. **Add Batch File Path to System Environment Variables:**
   - Copy the path to the directory containing `django_helper.bat`.
   - Open the Start Menu, search for "Environment Variables," and select "Edit the system environment variables."
   - In the System Properties window, click the "Environment Variables" button.
   - In the Environment Variables window, locate the `Path` variable in the "System variables" section, and click "Edit."
   - Click "New" and add the path to the directory containing `django_helper.bat`.
   - Click "OK" to close all dialog boxes.

4. **Execute the Module:**
   - Open any terminal or Command Prompt and run:
     ```bash
     django_helper.bat
     ```
   - For convenience, you can rename the batch file to something shorter, like `help_dj.bat`, and update the path in the system environment variables accordingly. This will make it easier to call and remember.

## 🐧 Usage and Setup in Linux
1. **Check if Python is installed**: Some Linux distributions come with Python pre-installed. You can check if Python is already installed by opening a terminal and typing:

```bash
python --version
```

If Python is installed, it will display the version number. If not, you'll see a message indicating that the command was not found.

2. **Install Python**: If Python is not installed, you can install it using your distribution's package manager. The package manager varies depending on the Linux distribution you're using:

   - **Debian/Ubuntu**:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

   - **Fedora**:
     ```bash
     sudo dnf install python3
     ```

   - **CentOS/RHEL**:
     ```bash
     sudo yum install python3
     ```

   - **Arch Linux**:
     ```bash
     sudo pacman -S python
     ```

3. **Verify installation**: After installation, verify that Python was installed correctly by running:
   ```bash
   python3 --version
   ```

   This should display the version number of the Python interpreter you just installed.
4. **Clone the Project:**
   - Navigate to the desired location and clone the Django Helper project:
     ```bash
     git clone https://github.com/Ramachandra-2k96/Django-helper.git
     ```
5. Create a script named `help_dj`:(Location of file will be different for you)
   - ```
     nano help_dj
     ```
     inside the file write this:
   ```bash 
   #!/bin/bash
   python /home/user/Desktop/django_helper.py
   ```
7. Save the script to `/usr/local/bin`:(By default most of the users system have this)
   ```bash
   sudo mv help_dj /usr/local/bin
   ```
8. Make the script executable:
   ```bash
   sudo chmod +x /usr/local/bin/help_dj
   ```
9. Now, you can run `help_dj` from any directory in the terminal:
 - Navigate to deisred location in terminal where you want to create your project and try the commands 
   ```bash
   help_dj
   ```
## 📞 Contact for Support

We're here to assist you every step of the way. If you encounter any issues, have suggestions for improvement, or simply want to reach out, please feel free to contact us:

- **Email**: [ramachandraudupa.sangamone@gmail.com](mailto:ramachandraudupa.sangamone@gmail.com)
- **GitHub Issues**: [Report issues here](https://github.com/Ramachandra-2k96/Django-helper/issues)
- **LinkedIn**: [Connect with us](https://in.linkedin.com/in/ramachandra-udupa)

---

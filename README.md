# GDG Website
A website for GDG JSS Noida

###Prerequisites

1. Pip
> sudo easy_install pip

2. Virtual Environment 
> pip install virtualenv

###Installation

1. Clone the repository
> git clone https://github.com/GDG-JSS-NOIDA/gdg_website.git

2. Migrate to the programmr folder
> cd gdg_website/gdg_website

3. Create Virtual Enviroment
> virtualenv venv

4. Start Virtual Environment
> source venv/bin/activate

5. Install requirements
> pip install -r ../requirements.txt

6. Create SuperUser
> python manage.py createsuperuser

7. Start Server
> python manage.py runserver
from ubuntu:precise  
  
maintainer Pini Reznik <p.reznik@uglyduckling.nl>  
  
run echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
run apt-get update  
run apt-get install -y build-essential git  
run apt-get install -y python python-dev python-setuptools  
run apt-get install -y nginx supervisor  
run easy_install pip  
  
# install uwsgi now because it takes a little while  
run pip install --no-use-wheel uwsgi  
  
# install nginx  
run apt-get install -y python-software-properties  
run apt-get update  
RUN add-apt-repository -y ppa:nginx/stable  
run apt-get install -y sqlite3  
  
# install our code  
add . /home/docker/code/  
  
# setup all the configfiles  
run echo "daemon off;" >> /etc/nginx/nginx.conf  
run rm /etc/nginx/sites-enabled/default  
run ln -s /home/docker/code/nginx-app.conf /etc/nginx/sites-enabled/  
run ln -s /home/docker/code/supervisor-app.conf /etc/supervisor/conf.d/  
  
# run pip install  
# run pip install --no-use-wheel -r /home/docker/code/app/requirements.txt  
run pip install --no-use-wheel django  
  
# install django, normally you would remove this step because your project
would already  
# be installed in the code/app/ directory  
# run django-admin.py startproject website /home/docker/code/app/  
expose 8000  
# cmd ["supervisord", "-n"]  
# cmd ["python manage.py", "runserver 0.0.0.0:8000"]a  
cmd ["./startup.sh"]  


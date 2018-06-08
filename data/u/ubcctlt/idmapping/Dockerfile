FROM ubuntu:trusty  
  
maintainer compass  
  
RUN apt-get update  
RUN apt-get install -y build-essential  
RUN apt-get install -y python python-dev python-setuptools  
RUN apt-get install -y supervisor  
RUN easy_install pip  
  
# install uwsgi now because it takes a little while  
RUN pip install uwsgi  
  
# install nginx  
RUN apt-get install -y python-software-properties  
RUN apt-get update  
RUN apt-get install -y nginx  
  
# install our code and requirement  
RUN mkdir /code  
ADD requirements /code/requirements  
WORKDIR /code  
RUN pip install -r requirements/dev.txt  
ADD . /code/  
  
# setup all the config files  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
RUN ln -s /code/docker/nginx-app.conf /etc/nginx/sites-enabled/  
RUN rm -f /etc/supervisor/supervisord.conf  
RUN ln -s /code/docker/supervisord.conf /etc/supervisor/supervisord.conf  
RUN ln -s /code/docker/supervisor-app.conf /etc/supervisor/conf.d/  
  
# Create log dir/file  
RUN mkdir -p logs  
RUN touch logs/apps_info.log  
RUN touch logs/apps_debug.log  
RUN touch logs/trace.log  
RUN touch logs/events.log  
RUN touch logs/errors.log  
  
# Collect static files  
RUN mkdir -p /code/volatile/static  
RUN python manage.py collectstatic --noinput  
  
expose 80  
cmd ["supervisord", "-n"]  


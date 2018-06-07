# This is a base image for django projects. It is based on the  
# python base image (which in turn is based on debian). You should  
# use the FROM dockerfile directive to inherit from this file  
# and then install your requirements like this:  
#  
# ADD REQUIREMENTS.txt /REQUIREMENTS.txt  
# RUN pip install -r /REQUIREMENTS.txt  
# RUN pip install uwsgi  
#  
# This image makes some other assumptions in particular:  
#  
# * nodejs / npm / yuglify are installed to compress django resources  
# * uwsgi runs on port 8080  
# * uwsgi is set up to serve the django project out of
/home/web/django_project  
# * the WORKDIR will be set to /home/web/django_project  
# * uwsgi will serve up static resources from /home/web/django_project/static  
# * uwsgi will serve up media resources from /home/web/django_project/media  
# * Your project is mounted into /home/web/django_project from a docker volume  
#  
#  
# NOTE: Django itself is not installed in this image - you must add it in your  
# REQUIREMENTS.txt file.  
#  
# Tim Sutton, December 2014  
FROM python:2.7  
MAINTAINER Tim Sutton<tim@linfiniti.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
#RUN ln -s /bin/true /sbin/initctl  
# Use local cached debs from host (saves your bandwidth!)  
# Change ip below to that of your apt-cacher-ng host  
# Or comment this line out if you do not with to use caching  
ADD 71-apt-cacher-ng /etc/apt/apt.conf.d/71-apt-cacher-ng  
RUN apt-get -y update  
RUN apt-get -y install \  
python-gdal \  
python-geoip \  
npm \  
nodejs \  
rpl  
RUN npm -g install yuglify  
  
# Debian is messed up and aliases node as nodejs  
# So when yuglify is installed it references the wrong node binary...  
# lets fix that here...  
RUN rpl "env node" "env nodejs"
/usr/local/lib/node_modules/yuglify/bin/yuglify  
  
ADD uwsgi.conf /uwsgi.conf  
  
# Open port 8080 as we will be running our uwsgi socket on that  
EXPOSE 8080  
WORKDIR /home/web/django_project  
  
# Under normal usage you would supply no additional params and  
# use nginx on the host to forward in the traffic.  
# Entrypoint is preferred but we use CMD  
# as fig run does not currently correctly  
# overload entrypoint  
CMD ["uwsgi", "--ini", "/uwsgi.conf"]  


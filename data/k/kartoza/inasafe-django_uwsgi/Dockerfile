#--------- Generic stuff all our Dockerfiles should start with so we get
caching ------------  
# Note this base image is based on debian  
FROM kartoza/django-base  
MAINTAINER Tim Sutton<tim@kartoza.com>  
  
RUN apt-get update -y; apt-get -y --force-yes install yui-compressor  
  
# Open port 8080 as we will be running our uwsgi socket on that  
EXPOSE 8080  
ADD REQUIREMENTS.txt /REQUIREMENTS.txt  
RUN pip install -r /REQUIREMENTS.txt  
RUN pip install uwsgi  
  
# Install Gettext  
RUN apt-get update -y; apt-get install -y gettext  
  
# Clone source code  
RUN mkdir -p /home/src/  
RUN mkdir -p /home/web/  
WORKDIR /home/src  
ARG INASAFE_DJANGO_TAG=develop  
RUN git clone \--branch ${INASAFE_DJANGO_TAG} \--depth 1
https://github.com/inasafe/inasafe-django.git  
  
# Copy only django_project folder  
RUN mkdir -p /home/web  
RUN cp -r inasafe-django/django_project /home/web/  
  
WORKDIR /home/web/django_project  
  
ADD entry-point.sh /entry-point.sh  
CMD ["/entry-point.sh"]  


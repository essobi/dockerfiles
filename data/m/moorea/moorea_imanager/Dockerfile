############################################################  
# Dockerfile to build Flask App  
# Based on  
############################################################  
  
# Set the base image  
FROM ubuntu:latest  
  
# File Author / Maintainer  
MAINTAINER carlos@moorea.io  
  
RUN apt-get update && apt-get install -y apache2 \  
libapache2-mod-wsgi \  
build-essential \  
python \  
python-dev\  
python-pip \  
vim \  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# Copy over and install the requirements  
# COPY ./app/requirements.txt /var/www/apache-flask/app/requirements.txt  
# RUN pip install -r /var/www/apache-flask/app/requirements.txt  
  
# Copy over the apache configuration file and enable the site  
# COPY ./apache-flask.conf /etc/apache2/sites-available/apache-flask.conf  
# RUN a2ensite apache-flask  
# RUN a2enmod headers  
  
# Copy over the imanager code  
COPY . /var/sources/moorea_imanager  
  
# COPY ./run.py /var/www/apache-flask/run.py  
# COPY ./app /var/www/apache-flask/app/  
  
# RUN a2dissite 000-default.conf  
# RUN a2ensite apache-flask.conf  
  
EXPOSE 80  
  
WORKDIR /var/www/moorea_imanager  
  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND


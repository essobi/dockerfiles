FROM ubuntu:trusty  
  
MAINTAINER David J <davidj@softcom.com>  
  
RUN ln -snf /bin/bash /bin/sh  
  
# Copy setup script to system  
COPY setup.sh /usr/local/bin/django-nginx-setup  
RUN chmod +x /usr/local/bin/django-nginx-setup  
  
# Replace apt sources.list to fetch packages from AWS EC2  
RUN sed -i 's/archive.ubuntu.com/us-east-1.ec2.archive.ubuntu.com/'
/etc/apt/sources.list  
  
# Update and upgrade system  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update &&
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade  
  
# Install dependencies for building python packages (add any additional here
if necessary)  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential python
python-dev libmysqlclient-dev libpq-dev libssl-dev libffi-dev python-
setuptools python-pip qt5-default libqt5webkit5-dev python-lxml xvfb nginx
supervisor  
  
# Install UWSGI and virtualenv globally  
RUN pip install uwsgi  
RUN pip install virtualenv  
  
# Create virtualenv  
WORKDIR /.virtualenv  
RUN virtualenv venv  
  
WORKDIR /app  
  
EXPOSE 80  
# Run user supplied script with information about Django project  
ENTRYPOINT ["sh", "/app/start.sh"]  


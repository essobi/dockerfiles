# Dockerfile for marconi-dev-env  
FROM ubuntu  
MAINTAINER Mike Panetta <mike.panetta@rackspace.com>  
  
# make sure the package repository is up to date  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get -y update  
  
# Add mongo repo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/mongodb.list  
RUN apt-get -y update  
  
# Install requirements  
RUN apt-get -y install python-pip python-dev git memcached mongodb-10gen gcc
make vim-nox emacs openssh-server netcat  
  
# Install marconi  
RUN pip install -e git+https://github.com/openstack/marconi#egg=marconi  
  
# Install marconi configs  
ADD /marconi.conf /etc/marconi/  
ADD /doit.sh /  
RUN chmod 700 /doit.sh  
  
# Install some wsgi servers and tools  
RUN pip install gunicorn uwsgi httpie  
  
# Open up the required ports for API access  
EXPOSE 80 443 27017  
# Set up env for mongo  
RUN mkdir -p /data/db  
  
# Do it!  
#ENTRYPOINT ["/bin/bash"]  
ENTRYPOINT ["/doit.sh"]  
  


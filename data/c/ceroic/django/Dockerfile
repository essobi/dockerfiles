FROM ceroic/python-base:3.5  
MAINTAINER Ceroic <ops@ceroic.com>  
  
# We also install the debian jessie backports repo so we can run updated
versions.  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" > \  
/etc/apt/sources.list.d/jessie-backports.list  
  
# We install nginx since we know this is how we deploy Django apps  
RUN apt-get update && apt-get install -y -t jessie-backports\  
daemontools \  
nginx  
  
COPY ./bin/init.sh /opt/ceroic/applications/django/bin/init.sh  
  
# Add a directory for use with envdir  
RUN mkdir -p /etc/env  
  
# We assume there is a requirements file in the root of the project.  
ONBUILD COPY requirements.txt /usr/src/app/requirements.txt  
ONBUILD RUN pip install -r requirements.txt  
  
ENTRYPOINT ["/opt/ceroic/applications/django/bin/init.sh"]  


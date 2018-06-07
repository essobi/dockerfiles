###========================================================================  
### File: Dockerfile  
###  
### Author(s): Enrique Fernandez <efcasado@gmail.com>  
###========================================================================  
FROM centos:6  
MAINTAINER Enrique Fernandez <efcasado@gmail.com>  
  
# Graphite port  
EXPOSE 8080:8080  
# Carbon plain-text port  
EXPOSE 2003:2003  
# Carbon pickle port  
EXPOSE 2004:2004  
# Install Graphite  
RUN yum install -y epel-release && \  
yum install -y \  
supervisor \  
net-snmp \  
perl \  
bitmap \  
bitmap-fonts \  
pycairo \  
mod_wsgi \  
python-devel \  
python-pip \  
git \  
which \  
gcc-c++ && \  
yum clean all && \  
pip install 'django<1.6' && \  
pip install 'Twisted<12' && \  
pip install django-tagging==0.3.6 && \  
pip install whisper==0.9.13 && \  
pip install graphite-web==0.9.13 && \  
pip install carbon==0.9.13  
  
# Configure Graphite  
ADD opt/graphite/ /opt/graphite/  
ADD etc/httpd/ /etc/httpd/  
ADD etc/init.d/ /etc/init.d/  
RUN cd /opt/graphite/webapp/graphite && \  
python manage.py syncdb --noinput  
  
# Configure supervisord  
COPY usr/etc/supervisord.conf /usr/etc/supervisord.conf  
  
COPY ./docker-entrypoint.sh docker-entrypoint.sh  
ENTRYPOINT [ "./docker-entrypoint.sh" ]


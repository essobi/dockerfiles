# Centos7 with with django and node + grunt + bower  
FROM centos:7  
MAINTAINER Marcos Sánchez <arkanus@gmail.com>  
  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
RUN yum upgrade -y  
RUN yum install -y \  
python-pip \  
MySQL-python \  
mysql-devel \  
gcc \  
python-devel \  
python-setuptools \  
mariadb \  
git \  
npm  
  
RUN pip install \  
django==1.7.4 \  
django-extensions==1.5 \  
iPython \  
Werkzeug  
  
RUN npm -g install grunt-cli bower  
  
ADD example /djangoapp  
WORKDIR /djangoapp  
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]  


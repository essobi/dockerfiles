FROM python:2  
MAINTAINER lucas6246@gmail.com  
  
RUN export LANG=en_US.UTF-8 \  
&& apt-get update && apt-get install -y \  
sudo \  
adduser \  
antiword \  
graphviz \  
ghostscript \  
poppler-utils \  
  
#Requirements for the pip install  
#For python-ldap2  
libldap2-dev \  
libsasl2-dev  
  
ADD requirements.txt /  
RUN pip install -r /requirements.txt  
  
# create the odoo user  
RUN adduser \--home=/opt/odoo --disabled-password --gecos ""
\--shell=/bin/bash odoo  


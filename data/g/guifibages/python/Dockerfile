FROM python:3  
MAINTAINER Ignacio Torres Masdeu <i@itorres.net>  
  
# Mimics python:3-onbuild except for the inclusion of ldap configuration and
network tools  
COPY ldap.conf /etc/ldap/ldap.conf  
COPY certs/* /usr/local/share/ca-certificates/  
RUN /usr/sbin/update-ca-certificates  
  
RUN apt-get update && \  
apt-get install -y libldap2-dev libsasl2-dev mtr-tiny traceroute  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN pip install --no-cache-dir -r requirements.txt  
  
ONBUILD COPY . /usr/src/app  


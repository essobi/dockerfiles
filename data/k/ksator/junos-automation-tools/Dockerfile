FROM ubuntu:14.04  
MAINTAINER Khelil Sator <ksator@juniper.net>  
##########################################################  
RUN apt-get update && apt-get install -y python-dev \  
libxml2-dev python-pip libxslt1-dev build-essential \  
libssl-dev libffi-dev git  
RUN pip install cryptography==1.2.1 junos-eznc==1.3.1 \  
jxmlease wget ansible==2.1.0.0 junos-netconify jsnapy \  
requests ipaddress pytest pytest-cov pyang pyangbind  
RUN ansible-galaxy install Juniper.junos  
  
WORKDIR /project  


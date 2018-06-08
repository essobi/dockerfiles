FROM centos:centos6  
MAINTAINER Jodie Belgrave  
  
# General Stuff  
RUN yum -y install wget gcc openssl openssl-devel  
RUN wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN rpm -Uvh epel-release-6-8.noarch.rpm  
  
# Install Java  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.rpm  
RUN rpm -Uvh jdk-8u25-linux-x64.rpm  
  
# Install PyMongo  
RUN yum -y install python-pip gcc python-devel  
RUN pip install pymongo  
  
# Environment Variables  
ENV mongo_addresses 10.1.42.1  
ENV mongo_database minestack  
  
ENV rabbit_addresses 10.1.42.1  
ENV rabbit_username guest  
ENV rabbit_password guest  
  
ENV server_id NULL  
  
# Copy Run Files  
RUN mkdir /minestack  
ADD setup.py /minestack/setup.py  
  
# Expose Port  
EXPOSE 25565  
# Run  
WORKDIR /minestack  
ENTRYPOINT ["python", "-u", "setup.py"]  


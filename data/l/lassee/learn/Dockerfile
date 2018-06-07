#  
#Flask App Dockerfile  
# Pull base image.  
FROM centos:7.0.1406  
# Build commands  
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc
python-devel git  
RUN easy_install pip  
RUN mkdir /opt/learn  
WORKDIR /opt/learn  
ADD requirements.txt /opt/learn  
MAINTAINER Aaron Michelson "michnoam@gmail.com"  
RUN pip install -r requirements.txt  
ADD . /opt/learn  
  
# Define default command.  
CMD ["python", "manage.py", "runserver"]  


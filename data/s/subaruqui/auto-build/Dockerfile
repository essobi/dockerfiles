FROM python:3.6.2  
  
RUN apt-get update  
  
RUN apt-get install -y git  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y libffi-dev  
RUN apt-get install -y libsasl2-dev  
RUN apt-get install -y libldap2-dev  
RUN apt-get install -y python-ldap  
# update pip  
RUN apt-get install -y libxml2-dev  
RUN apt-get install -y libxmlsec1-dev  
RUN apt-get install -y libmemcached-dev  
RUN mkdir /code  
ADD requirements.txt /code  
WORKDIR /code  
RUN pip install -r requirements.txt  
RUN pip install django-cors-headers  
EXPOSE 8000  


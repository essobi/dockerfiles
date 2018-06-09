FROM python:3.6.1  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update \  
&& apt-get install -y libxml2-dev libxmlsec1-dev libxmlsec1-openssl
libsasl2-dev python-dev libldap2-dev libssl-dev  
RUN mkdir /code  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  


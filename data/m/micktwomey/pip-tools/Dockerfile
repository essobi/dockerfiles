FROM python:2.7.13-alpine  
MAINTAINER Michael Twomey <mick@twomeylee.name>  
  
COPY requirements.txt /requirements.txt  
RUN pip install -U setuptools pip wheel \  
&& pip install -r /requirements.txt  
  
WORKDIR /src  
  
CMD ["pip-compile", "--upgrade", "requirements.in"]  


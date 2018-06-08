FROM python:3.6-slim  
  
# 5000 for uWSGI, 5001 for monitoring - user wsgitop to connect to port  
EXPOSE 5000 5001  
# Copying necessary files for Andes API  
COPY system/api/code /andes/system/api/code  
COPY system/api/requirements_container.txt /andes/system/api  
COPY system/api/templates /andes/system/api/templates  
COPY system/api/*.ini /andes/system/api  
  
WORKDIR /andes/system/api  
  
# Getting packages for API  
RUN apt-get update \  
&& apt-get install build-essential -y \  
&& pip3 install -r requirements_container.txt \  
&& apt-get clean  
  
CMD ["uwsgi","uwsgi.ini"]  


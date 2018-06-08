#  
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
FROM python:3  
RUN apt-get update \  
&& apt-get install -y python3-dev  
  
RUN pip install --upgrade pip \  
&& pip install -U \  
pytest \  
python-dateutil \  
&& mkdir -p /var/www  
  
WORKDIR /var/www  


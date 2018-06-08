#  
# Flexget Dockerfile  
#  
# https://github.com/kmb32123/flexget-dockerfile  
#  
# Pull base image.  
FROM python:3.6-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
VOLUME ["/flexget"]  
VOLUME ["/input"]  
VOLUME ["/output"]  
  
WORKDIR /flexget  
  
CMD rm -f /flexget/.config-lock && flexget daemon start  


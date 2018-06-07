# Docker file for med2img  
FROM fnndsc/ubuntu-python3:latest  
MAINTAINER fnndsc "dev@babymri.org"  
ENV APPROOT="/usr/src/med2img" VERSION="0.1"  
COPY ["med2img", "${APPROOT}"]  
COPY ["requirements.txt", "${APPROOT}"]  
  
WORKDIR $APPROOT  
  
RUN apt-get update \  
&& apt-get install -y python3-tk \  
&& pip install -r requirements.txt  
  
CMD ["med2img.py", "--help"]  


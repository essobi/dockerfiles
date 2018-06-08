# Docker file for the simplefsapp  
FROM fnndsc/ubuntu-python3:latest  
MAINTAINER fnndsc "dev@babymri.org"  
ENV APPROOT="/usr/src/simplefsapp" VERSION="0.1"  
COPY ["simplefsapp", "${APPROOT}"]  
COPY ["requirements.txt", "${APPROOT}"]  
  
WORKDIR $APPROOT  
  
RUN pip install -r requirements.txt  
  
CMD ["simplefsapp.py", "--help"]  


# Docker file for the simpledsapp  
FROM fnndsc/ubuntu-python3:latest  
MAINTAINER fnndsc "dev@babymri.org"  
ENV APPROOT="/usr/src/simpledsapp" VERSION="0.1"  
COPY ["simpledsapp", "${APPROOT}"]  
COPY ["requirements.txt", "${APPROOT}"]  
  
WORKDIR $APPROOT  
  
RUN pip install -r requirements.txt  
  
CMD ["simpledsapp.py", "--help"]  


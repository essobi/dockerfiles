# Docker file for the simpledsapp  
FROM fnndsc/ubuntu-python3:latest  
MAINTAINER fnndsc "dev@babymri.org"  
ENV APPROOT="/usr/src/s3retrieve" VERSION="0.1"  
COPY ["s3retrieve", "${APPROOT}"]  
COPY ["requirements.txt", "${APPROOT}"]  
  
WORKDIR $APPROOT  
  
RUN pip install -r requirements.txt  
  
CMD ["s3retrieve.py", "--help"]  


# Docker file for the reconall plugin app  
FROM fnndsc/ubuntu-python3:latest  
MAINTAINER fnndsc "dev@babymri.org"  
ENV APPROOT="/usr/src/reconall" VERSION="0.1"  
COPY ["reconall", "${APPROOT}"]  
COPY ["requirements.txt", "${APPROOT}"]  
  
WORKDIR $APPROOT  
  
RUN pip install -r requirements.txt  
  
CMD ["reconall.py", "--help"]  


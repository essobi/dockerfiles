FROM python:3.5  
MAINTAINER Tom Daff "tdd20@cam.ac.uk"  
# source tree  
ADD . /opt/src/errp  
WORKDIR /opt/src/errp  
  
# Ensures that pytest is also installed  
RUN pip install .[test]  
  
# Stop images being buit if tests fail  
RUN pytest -vv  
  
# Default Flask port  
EXPOSE 5000  
CMD errpd  
#CMD errpd -s http://source.com/data.file  


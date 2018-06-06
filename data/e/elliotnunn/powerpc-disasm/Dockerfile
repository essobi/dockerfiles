FROM python:3.5  
MAINTAINER Elliot Nunn <elliotnunn@fastmail.com>  
  
RUN pip install networkx capstone blist  
  
COPY *.py /usr/local/lib/  
  
ENV PYTHONPATH /usr/local/lib:$PYTHONPATH  


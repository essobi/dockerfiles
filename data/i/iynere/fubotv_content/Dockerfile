FROM circleci/python:2.7.13  
  
USER root  
  
RUN apt-get update  
RUN apt-get install dos2unix  
RUN pip install awscli csvkit  
  
USER circleci


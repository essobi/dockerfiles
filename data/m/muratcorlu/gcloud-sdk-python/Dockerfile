FROM python:2.7  
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-jessie main" |
tee /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
RUN apt-get update && apt-get install google-cloud-sdk google-cloud-sdk-app-
engine-python -y  


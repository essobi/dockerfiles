# To shorted build time  
# build from the previously build image  
# This will reduce the time needed to create  
# installing al packages  
# to build image from scratch use this base image FROM python:3.5  
#FROM python:2.7  
FROM tumacredo/inclusivity-sms  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN [ -f ./requirements.txt ] && pip install -r ./requirements.txt|| echo
"Requirements file not found"  
  
CMD ["/bin/bash", "./vumi.sh"]  


#  
# dockerhub/trainingwheelsh  
# Testing a simple command line script deployment  
#  
FROM ubuntu  
MAINTAINER "Cloud Orchestration"  
LABEL version="0.1"  
  
#ADD places our script into the Docker Container  
ADD trainingwheel.sh /root/trainingwheel.sh  
  
# COPY trainingwheel.sh /bin/sh/trainingwheel.sh  
#Entrypoint declares a defult application  
CMD echo "With Entrypoint we now cause the install to start our script here"  
ENTRYPOINT /root/trainingwheel.sh  
  
# RUN mkdir train  
# COPY trainingwheel.sh train  
# CMD train/trainingwheel.sh  


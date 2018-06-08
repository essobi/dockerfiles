FROM ubuntu:14.04  
MAINTAINER Leandro Pineda <leandropineda.lp@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
openjdk-7-jre \  
unzip  
  
# Create a new user "developer".  
# It will get access to the X11 session in the host computer  
ENV uid=1000  
ENV gid=${uid}  
  
COPY create_user.sh /  
  
CMD /create_user.sh && sudo -H -u developer /bin/bash  


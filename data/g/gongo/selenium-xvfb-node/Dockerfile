FROM ubuntu:trusty  
MAINTAINER Wataru MIYAGUNI "gonngo@gmail.com"  
# Install packages  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y openjdk-7-jre-headless firefox xvfb fonts-ipafont-
gothic  
  
# Download selenium server  
RUN curl http://selenium-release.storage.googleapis.com/2.42/selenium-server-
standalone-2.42.2.jar -o /opt/selenium-server.jar  
  
# Start selenium `node` server  
Add ./start.sh /opt/start.sh  
RUN chmod +x /opt/start.sh  
CMD /opt/start.sh  


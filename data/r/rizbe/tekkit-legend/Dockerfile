# This Dockerfile is used to build an image containing Minecraft Tekkit  
FROM ubuntu:trusty  
MAINTAINER Rizbe  
  
  
# Make sure the package repository is up to date.  
RUN apt update  
RUN apt -y upgrade  
  
#Install Java  
RUN apt install openjdk-7-jre-headless unzip wget -y  
  
# Add user minecraft  
RUN adduser --quiet minecraft  
RUN mkdir /opt/tekkit  
RUN chown -R minecraft /opt/tekkit  
  
#Download Tekkit Legends  
RUN wget -O /tmp/tekkit.zip
http://servers.technicpack.net/Technic/servers/tekkit-
legends/Tekkit_Legends_Server_v1.1.1.zip  
RUN unzip /tmp/tekkit.zip -d /opt/tekkit  
RUN chmod +x /opt/tekkit/start.sh  
RUN chown -R minecraft /opt/tekkit  
  
VOLUME ["/opt/tekkit"]  
EXPOSE 25565  
WORKDIR /opt/tekkit  
USER minecraft  
ENTRYPOINT ["/bin/sh","/opt/tekkit/start.sh"]  


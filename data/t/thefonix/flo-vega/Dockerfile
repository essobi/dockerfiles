# ----------------------------------  
# CorinthMC Core Dockerfile  
# Environment: Java  
# Version: 1.0.0  
# ----------------------------------  
#Refer to the Java Container  
FROM openjdk:8-jdk-alpine  
  
#Author Information  
MAINTAINER Fonix Hardcastle, <me@fonix.online>  
  
#Install and update Alpine Dependencies for the CorinthMC Containers.  
RUN apk update \  
&& apk upgrade \  
&& apk add \--no-cache --update curl ca-certificates zip unzip openssl openssh
curl sudo git tar bash sqlite \  
&& adduser -u 1000 -D -h /home/container container \  
&& echo "ALL ALL = (ALL) NOPASSWD: ALL" > /etc/sudoers \  
&& chown root:root /usr/bin \  
&& chmod u+s /usr/bin/sudo  
  
#User to Run the DockerFile as  
USER container  
ENV  USER container  
ENV HOME /home/container  
  
#Set the work Directory  
WORKDIR /home/container  
  
#Copy Process of the EntryPoint File  
COPY ./entrypoint.sh /entrypoint.sh  
  
#Run the entryPoint File  
CMD ["/bin/bash", "/entrypoint.sh"]  


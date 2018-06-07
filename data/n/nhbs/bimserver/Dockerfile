#  
# 2017 © Headcount Solutions Ltd.  
# See 'LICENCE.md' in the project root for more information.  
#  
FROM tomcat:9-jre8  
MAINTAINER Neil Hyland <neil.hyland@bimandscan.com>  
  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get clean  
  
ENV BIMSERVER_VERSION "1.5.100"  
COPY ./scripts/Install.sh .  
RUN chmod +x ./Install.sh  
RUN ./Install.sh  
  
COPY ./scripts/default.policy /usr/local/tomcat/conf/default.policy  
COPY ./scripts/server.xml /usr/local/tomcat/conf/server.xml  
COPY ./scripts/context.xml /usr/local/tomcat/conf/context.xml  
  
EXPOSE 8080  
VOLUME /var/bimserver/home  
  


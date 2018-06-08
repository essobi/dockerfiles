FROM tomcat:latest  
  
MAINTAINER minanon  
  
ENV CATALINA_OPTS -server -Xmx256M -Xms64M -Xss32M -XX:NewSize=1M
-XX:MaxNewSize=16M -XX:SurvivorRatio=2 -XX:PermSize=128M -XX:MaxPermSize=128M  
  
RUN rm -rf /usr/local/tomcat/webapps/*  


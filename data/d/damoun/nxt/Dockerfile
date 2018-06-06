FROM java:8-jre  
  
MAINTAINER Damien Plenard "damien+docker@plenard.me"  
ADD https://bitbucket.org/JeanLucPicard/nxt/downloads/nxt-client-1.7.5.zip
/tmp/nxt-client.zip  
  
RUN unzip /tmp/nxt-client.zip -d /usr/local/  
WORKDIR /usr/local/nxt  
RUN echo 'nxt.allowedBotHosts=*' >> conf/nxt.properties  
RUN echo 'nxt.apiServerHost=0.0.0.0' >> conf/nxt.properties  
  
# clean  
RUN rm /tmp/nxt-client.zip  
  
EXPOSE 7876  
ENTRYPOINT ["java", "-jar", "nxt.jar"]  


FROM java:8-jre  
  
MAINTAINER ja "josecuore@gmail.com"  
ADD https://bitbucket.org/Jelurida/nxt-evaluation/downloads/nxt-eval-
client-1.11.5.zip /tmp/nxt-client.zip  
  
RUN unzip /tmp/nxt-client.zip -d /usr/local/  
WORKDIR /usr/local/nxt-eval  
RUN echo 'nxt.allowedBotHosts=*' >> conf/nxt.properties  
RUN echo 'nxt.apiServerHost=0.0.0.0' >> conf/nxt.properties  
RUN echo 'nxt.adminPassword=4u2%HveKAts5W4*6' >> conf/nxt.properties  
# clean  
RUN rm /tmp/nxt-client.zip  
  
EXPOSE 6876  
ENTRYPOINT ["java", "-jar", "nxt.jar"]  


FROM tomcat:8.0-jre8-alpine  
  
LABEL maintainer "alessandro.lucaferro@gmail.com"  
  
RUN rm -rf /usr/local/tomcat/webapps/*  
  
RUN sed -i -e 's/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=5/'
$JAVA_HOME/lib/security/java.security  
  
EXPOSE 8080  


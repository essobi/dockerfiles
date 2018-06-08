FROM openjdk:8-jre  
  
LABEL maintainer="Grégory Van den Borre vandenborre.gregory@hotmail.fr"  
  
RUN mkdir /yildiz  
  
RUN curl -LO https://bitbucket.org/yildiz-engine-
team/webapp/downloads/webapp.jar  
  
ENTRYPOINT ["java", "-jar", "/webapp.jar", "--
logging.config=/yildiz/logback.xml"]  


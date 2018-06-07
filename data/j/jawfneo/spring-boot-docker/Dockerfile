FROM daocloud.io/java:7  
MAINTAINER Florian Lopes <florian.lopes@outlook.com>  
  
VOLUME /tmp  
VOLUME /upload  
  
ENV APP_HOME /app  
ENV APP_JAR spring-boot-application.jar  
ENV profile prd  
  
COPY assets/* ${APP_HOME}/  
  
RUN chmod 755 ${APP_HOME}/entrypoint.sh  
  
RUN bash -c 'touch ${APP_HOME}/${APP_JAR}'  
  
ENTRYPOINT ["/app/entrypoint.sh"]  


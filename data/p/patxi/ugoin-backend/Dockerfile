FROM openjdk:latest  
WORKDIR /opt/docker  
ADD opt /opt  
RUN ["chown", "-R", "daemon:daemon", "."]  
USER daemon  
ENTRYPOINT ["bin/ugoin-backend", "-Dconfig.resource=prod.conf",
"-Dlogger.resource=prod-logger.xml"]  
CMD []  
RUN ["chmod", "+x", "/opt/docker/bin/ugoin-backend"]  


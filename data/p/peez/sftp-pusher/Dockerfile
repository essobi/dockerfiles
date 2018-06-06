FROM openjdk:8  
COPY ./ ./  
RUN chmod +x ./gradlew  
RUN ./gradlew installDist  
  
FROM alpine:latest  
RUN apk add --no-cache openjdk8-jre bash  
COPY \--from=0 ./build/install/foldersync/ /opt/foldersync/  
COPY \--from=0 ./src/main/docker/docker-entrypoint.sh /opt/docker-
entrypoint.sh  
  
RUN chmod +x /opt/docker-entrypoint.sh && mkdir /backuproot  
VOLUME /backuproot  
ENV SFTP_HOST= \  
SFTP_USER= \  
SFTP_PASS= \  
SFTP_PORT=22 \  
SFTP_ROOT=  
  
CMD ["/opt/docker-entrypoint.sh"]  
  


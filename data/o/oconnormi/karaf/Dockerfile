FROM alpine  
ENV APACHE_ARCHIVED_RELEASE=true  
ENV KARAF_VERSION=4.1.1  
ENV ARCHIVE_NAME=apache-karaf-${KARAF_VERSION}.tar.gz  
RUN apk add --no-cache curl tar gzip  
COPY scripts/* /scripts/  
RUN chmod 755 /scripts/*.sh  
RUN sh -c /scripts/downloadKaraf.sh  
RUN sh -c /scripts/unpackKaraf.sh  
  
FROM anapsix/alpine-java:jdk  
MAINTAINER oconnormi  
  
ENV KARAF_VERSION=4.0.7  
ENV ENTRYPOINT_HOME=/app/entrypoint  
ENV APP_HOME="/opt/karaf"  
  
COPY \--from=0 /opt/karaf /opt/karaf  
  
VOLUME /app/data /app/deploy /app/etc  
  
COPY entrypoint/* /app/entrypoint/  
  
EXPOSE 8101 8443 8181 1099 44444 5701 54327  
ENTRYPOINT ["/bin/bash", "-c", "/app/entrypoint/run"]  


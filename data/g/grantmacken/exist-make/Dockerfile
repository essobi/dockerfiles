  
# FROM grantmacken:exist-base as base  
FROM openjdk:9-jre-slim as jdk  
# exposes $JAVA_HOME  
# exec java resolves  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VCS_URL  
ARG VERSION  
  
LABEL maintainer="Grant Mackenzie <grantmacken@gmail.com>" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
wget \  
curl \  
expect \  
&& apt-get clean  
  
ENV EXIST_HOME /user/local/eXist  
ENV EXIST_DATA_DIR webapp/WEB_INF/data  
ENV MAX_MEMORY 512  
ENV INSTALL_PATH /grantmacken  
RUN mkdir -p $INSTALL_PATH  
WORKDIR $INSTALL_PATH  
COPY Makefile Makefile  
RUN make  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
EXPOSE 8080  
# # VOLUME $EXIST_DATA_DIR  
WORKDIR $EXIST_HOME  
ENTRYPOINT ["java", "-Djava.awt.headless=true", "-jar", "start.jar", "jetty"]  


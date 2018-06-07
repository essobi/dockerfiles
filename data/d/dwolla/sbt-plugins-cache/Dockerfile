FROM openjdk:8-jdk-alpine AS downloader  
LABEL maintainer="Dwolla Dev <dev+sbt@dwolla.com>"  
LABEL org.label-schema.vcs-url="https://github.com/Dwolla/docker-sbt-version-
cache"  
  
USER root  
ENV SBT_VERSION=1.1.1 \  
SBT_HOME=/usr/local/sbt  
ENV PATH=${SBT_HOME}/bin:${PATH}  
  
COPY fake-project /fake-project  
  
RUN apk add --update --no-cache curl ca-certificates bash git  
RUN curl -sL /tmp/sbt-${SBT_VERSION}.tgz
"https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz"
| \  
gunzip | tar -x -C /usr/local  
  
RUN cd /fake-project && \  
sbt -Dsbt.log.noformat=true clean +compile  
  
FROM scratch  
COPY \--from=downloader /usr/local/sbt /usr/local/sbt  
COPY \--from=downloader /root/.ivy2 /root/.ivy2  
COPY \--from=downloader /root/.sbt /root/.sbt  


FROM openjdk:8-jdk-alpine AS downloader  
LABEL maintainer="Dwolla Dev <dev+sbt@dwolla.com>"  
LABEL org.label-schema.vcs-url="https://github.com/Dwolla/docker-sbt-version-
cache"  
  
USER root  
ENV SBT_VERSION=1.1.5 \  
SBT_HOME=/usr/local/sbt  
ENV PATH=${SBT_HOME}/bin:${PATH}  
  
COPY fake-project /fake-project  
  
RUN apk add --update --no-cache curl ca-certificates bash  
RUN curl -sL /tmp/sbt-${SBT_VERSION}.tgz
"https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz"
| \  
gunzip | tar -x -C /usr/local  
  
RUN cd /fake-project && \  
for version in 0.13.16 0.13.17 1.0.4 1.1.0 1.1.1 1.1.2 1.1.4 1.1.5; do \  
echo sbt.version=${version} > project/build.properties && \  
sbt -Dsbt.log.noformat=true clean +compile; \  
done  
  
FROM scratch  
COPY \--from=downloader /usr/local/sbt /usr/local/sbt  
COPY \--from=downloader /root/.ivy2 /root/.ivy2  
COPY \--from=downloader /root/.sbt /root/.sbt  


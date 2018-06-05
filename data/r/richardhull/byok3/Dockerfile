FROM jfisbein/alpine-oracle-jdk9:latest  
MAINTAINER Richard Hull <rm_hull@yahoo.co.uk>  
  
ARG SCALA_VERSION=2.12  
ARG
SBT_DOWNLOAD_URL=https://github.com/sbt/sbt/releases/download/v1.1.4/sbt-1.1.4.tgz  
  
RUN apk add --no-cache bash  
  
RUN apk add --no-cache --virtual=build-dependencies curl && \  
curl -sL $SBT_DOWNLOAD_URL | gunzip | tar -x -C /usr/local && \  
ln -s /usr/local/sbt/bin/sbt /usr/local/bin/sbt && \  
chmod 0755 /usr/local/bin/sbt && \  
apk del build-dependencies && \  
rm -rf /tmp/* /var/cache/apk/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN \  
sbt web/assembly && \  
mv web/target/scala-$SCALA_VERSION/byok3-web.jar byok3-web.jar && \  
rm -rf target project/target ~/.ivy2  
  
EXPOSE 5000  
ENTRYPOINT ["java", "-jar", "byok3-web.jar"]


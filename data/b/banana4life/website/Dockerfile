FROM openjdk:8-jdk-alpine as build  
RUN apk update && \  
apk upgrade && \  
apk add sbt --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
RUN mkdir /build  
WORKDIR /build  
COPY . /build  
RUN sbt dist  
  
FROM openjdk:8-jre-alpine  
RUN apk update && \  
apk upgrade && \  
apk add unzip bash  
RUN mkdir /app  
WORKDIR /app  
COPY \--from=build /build/target/universal/website-*.zip /app.zip  
RUN unzip /app.zip && \  
rm /app.zip && \  
mv website-*/* . && \  
rmdir website-* && \  
rm -R share && \  
adduser -D -H -h /app banana4life && \  
chown -R banana4life:banana4life /app  
USER banana4life  
ENTRYPOINT ["bin/website"]


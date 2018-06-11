FROM alpine as download  
MAINTAINER Zoltan Dalmadi <dmz985@gmail.com>  
RUN apk add --no-cache curl unzip  
RUN curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/unlimited_jce_policy.zip "http://download.oracle.com/otn-
pub/java/jce/8/jce_policy-8.zip"  
RUN unzip -jo -d /tmp/jce /tmp/unlimited_jce_policy.zip  
  
FROM openjdk:jre-alpine  
COPY \--from=download /tmp/jce ${JAVA_HOME}/lib/security  


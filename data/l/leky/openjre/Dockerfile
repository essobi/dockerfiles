FROM leky/alpine:latest  
MAINTAINER leky <lekyzsj@gmail.com>  
  
ENV JAVA_VERSION="8u92" \  
JAVA_ALPINE_VERSION="8.92.14-r1" \  
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk/jre \  
PATH=${PATH}:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
RUN apk add --no-cache openjdk8-jre  
  
CMD ["java", "-version"]  


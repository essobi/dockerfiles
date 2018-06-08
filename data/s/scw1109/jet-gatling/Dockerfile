FROM java:8-jdk-alpine  
  
MAINTAINER Alan She <scw1109@gmail.com>  
  
ENV JET_GATLING_VERSION 0.5  
RUN mkdir -p /jet-gatling  
  
RUN apk add --update wget && \  
wget -q -O /jet-gatling/jet-gatling.jar \  
https://jitpack.io/com/github/scw1109/jet-gatling/$JET_GATLING_VERSION/jet-
gatling-$JET_GATLING_VERSION.jar  
  
ADD jet-gatling.sh /jet-gatling/jet-gatling.sh  
  
WORKDIR /jet-gatling  
  
VOLUME ["/jet-gatling/results", "/jet-gatling/user-files"]  
  
ENV PATH /jet-
gatling:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
ENTRYPOINT ["jet-gatling.sh"]  


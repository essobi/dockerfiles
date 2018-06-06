FROM openjdk:8-jre-alpine  
  
RUN apk add --no-cache tzdata ttf-dejavu \  
&& cp /usr/share/zoneinfo/America/Los_Angeles /etc/localtime \  
&& echo America/Los_Angeles > /etc/timezone \  
&& apk del tzdata \  
&& rm -rf /var/cache/apk/*  


FROM maven:3.5-jdk-8-alpine  
  
RUN apk add --no-cache \  
gawk jq libxml2-utils  
  
COPY .m2/settings.xml /root/.m2/settings.xml  
COPY assets /opt/resource  
COPY test /opt/resource/test  
  
RUN /opt/resource/test/test-all.sh  


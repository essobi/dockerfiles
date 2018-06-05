FROM openjdk:jre-alpine  
  
ENV CHECKSTYLE_VERSION 8.0  
  
RUN apk update && \  
apk --no-cache add openssl && \  
mkdir -p /opt/lib && \  
wget -q -O /opt/lib/checkstyle.jar
https://downloads.sourceforge.net/project/checkstyle/checkstyle/$CHECKSTYLE_VERSION/checkstyle-$CHECKSTYLE_VERSION-
all.jar && \  
apk del openssl  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
WORKDIR /workdir  
ENTRYPOINT ["docker-entrypoint.sh"]  


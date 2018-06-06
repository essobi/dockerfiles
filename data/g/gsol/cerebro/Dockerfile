FROM openjdk:8u151-jre-alpine  
MAINTAINER Global Solutions co., ltd.  
LABEL semver="0.4.0"  
  
ENV CEREBRO_VER=0.7.2  
WORKDIR cerebro  
RUN apk add --update --no-cache openssl tar bash && \  
wget -O -
https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VER}/cerebro-${CEREBRO_VER}.tgz
| tar xzv --strip-components 1 && \  
apk del openssl tar && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 9000  
ENTRYPOINT ["/cerebro/bin/cerebro"]  


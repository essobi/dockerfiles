FROM alpine  
MAINTAINER Tiago Caxias http://github.com/tcaxias  
  
ENV \  
TERM=xterm \  
PKGS="python openjdk8-jre-base" \  
DEPS="aria2" \  
APK="apk --update --cache" \  
PRESTO_VERSION="0.177"  
RUN \  
apk --no-cache --update add $PKGS $DEPS && \  
mkdir -p /app /var/presto/data && \  
aria2c -q -x5 -j5 -o /tmp/presto.tgz \  
http://uk.maven.org/maven2/com/facebook/presto/presto-
server/${PRESTO_VERSION}/presto-server-${PRESTO_VERSION}.tar.gz && \  
tar -f /tmp/presto.tgz -xzC /tmp/ && \  
mv /tmp/presto-*/* /app && \  
apk del $DEPS && \  
rm -rf /tmp/* /var/cache/apk/*  
  
WORKDIR /app/  
VOLUME /app/etc  
  
CMD [ "/app/bin/launcher", "run" ]  


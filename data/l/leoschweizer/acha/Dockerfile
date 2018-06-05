FROM alpine:3.3  
MAINTAINER Leo Schweizer <leonhard.schweizer@gmail.com>  
  
ENV ACHA_VERSION 0.2.5  
ENV ACHA_IP 0.0.0.0  
ENV ACHA_PORT 80  
ADD known_hosts /root/.ssh/known_hosts  
  
VOLUME .acha  
VOLUME /root/.ssh  
  
EXPOSE $ACHA_PORT  
  
ADD https://github.com/someteam/acha/releases/download/${ACHA_VERSION}/acha-
uber-${ACHA_VERSION}.jar /acha.jar  
  
RUN \  
apk --no-cache --update add java-cacerts openjdk7-jre && \  
rm /usr/lib/jvm/java-1.7-openjdk/jre/lib/security/cacerts && \  
ln -s /etc/ssl/certs/java/cacerts
/usr/lib/jvm/java-1.7-openjdk/jre/lib/security/cacerts  
  
CMD java -jar /acha.jar --ip 0.0.0.0 --port $ACHA_PORT \--dir .acha
${ACHA_PRIVATE_KEY:+ --private-key ${ACHA_PRIVATE_KEY}}  


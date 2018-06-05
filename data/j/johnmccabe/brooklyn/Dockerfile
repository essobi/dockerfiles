FROM gliderlabs/alpine:3.3  
RUN apk-install openjdk8-jre-base ; \  
apk-install bash ; \  
apk-install curl  
  
ENV VERSION 0.11.0  
ENV brooklyn.webconsole.security.users docker  
ENV brooklyn.webconsole.security.user.docker.password docker  
  
RUN curl -o apache-brooklyn.tar.gz -L
"https://www.apache.org/dyn/closer.lua?action=download&filename=brooklyn/apache-
brooklyn-${VERSION}/apache-brooklyn-${VERSION}-bin.tar.gz"; \  
tar zxf apache-brooklyn.tar.gz ; \  
rm -f apache-brooklyn.tar.gz  
  
WORKDIR /apache-brooklyn-${VERSION}-bin  
  
VOLUME [ "/root/.brooklyn", "/root/.ssh" , "/root/.brooklyn-persistance" ]  
  
EXPOSE 8081  
ENTRYPOINT ./bin/brooklyn launch --persist auto --persistenceDir
/root/.brooklyn-persistance


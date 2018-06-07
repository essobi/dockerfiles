FROM alpine:3.6  
MAINTAINER stefan.unterhofer@jollydays.com  
  
# Install AWS cli (see https://github.com/anigeo/docker-
awscli/blob/master/Dockerfile)  
RUN apk -Uuv add groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
# Install Java 8, curl and bash  
RUN apk --update add bash ca-certificates curl openjdk8-jre-base && rm -rf
/var/cache/apk/*  
ENV JAVA_HOME=/usr/lib/jvm/default-jvm  
  
# Install Bouncycastle Security Provider (fix for invalid prime number
connection error)  
# See http://stackoverflow.com/questions/6851461/java-why-does-ssl-handshake-
give-could-not-generate-dh-keypair-exception  
ENV BC_VERSION=jdk15on-154  
RUN curl -jksSL http://bouncycastle.org/download/bcprov-$BC_VERSION.jar >
$JAVA_HOME/jre/lib/ext/bcprov-$BC_VERSION.jar &&\  
curl -jksSL http://bouncycastle.org/download/bcprov-ext-$BC_VERSION.jar >
$JAVA_HOME/jre/lib/ext/bcprov-ext-$BC_VERSION.jar  
COPY java.security $JAVA_HOME/jre/lib/security/  
  
# Add dns config, see https://github.com/gliderlabs/docker-alpine/issues/11  
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
# Add Jolokia  
ENV JOLOKIA_VERSION 1.3.1  
ADD jolokia_opts /bin/  
RUN chmod 755 /bin/jolokia_opts && mkdir -p /opt/jolokia && wget
http://central.maven.org/maven2/org/jolokia/jolokia-jvm/1.3.1/jolokia-
jvm-1.3.1-agent.jar -O /opt/jolokia/jolokia.jar  
CMD java -jar /opt/jolokia/jolokia.jar --version  
  
# Add fabric8 scripts  
ENV CLASSPATH /maven/*:/maven  
RUN mkdir /maven  
EXPOSE 8778  
run mkdir /fabric8  
  
# Add NewRelic  
ENV NR_VERSION=3.31.0  
RUN curl https://download.newrelic.com/newrelic/java-agent/newrelic-
agent/$NR_VERSION/newrelic-agent-$NR_VERSION.jar > /fabric8/newrelic.jar &&\  
curl https://download.newrelic.com/newrelic/java-agent/newrelic-
agent/$NR_VERSION/newrelic.yml > /fabric8/newrelic.yml  
  
# add custom run script + newrelic  
ADD run.sh /fabric8/  
  
CMD [ "/fabric8/run.sh" ]  


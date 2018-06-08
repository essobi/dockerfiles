#  
# Alpine Linux - AMQ7 snapshot Dockerfile  
#  
FROM alpine:latest  
  
MAINTAINER Dominik Lenoch <dlenoch@redhat.com>  
  
USER root  
  
RUN apk update && apk upgrade && apk add \  
su-exec \  
tini \  
openjdk8-jre-base \  
libaio \  
wget \  
grep \  
&& rm -rf /var/cache/apk/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
  
# create artemis user without password and home dir  
RUN addgroup -S amq7 && adduser -s /bin/false -D -H amq7 -G amq7  
  
# Setup broker  
RUN \  
# Set sources  
REPO='https://repository.jboss.org/nexus/content/groups/public/org/jboss/rh-
messaging/AMQ7/A-MQ7/7.0.0-SNAPSHOT/' && \  
VERSION=$(wget -O - -o /dev/null $REPO/maven-metadata.xml | grep -oP
'(?<=<value>).*?(?=</value>)' | head -1) && \  
mkdir /opt && cd /opt && \  
wget -q $REPO/A-MQ7-$VERSION-bin.zip && \  
wget -q $REPO/A-MQ7-$VERSION-bin.zip.sha1 && \  
# Verify  
sha1sum A-MQ7-$VERSION-bin.zip | grep $(cat A-MQ7-$VERSION-bin.zip.sha1) && \  
# Unpack and create link  
unzip A-MQ7-$VERSION-bin.zip && \  
ln -s A-MQ7-7.0.0-SNAPSHOT A-MQ7 && \  
rm -rf A-MQ7-$VERSION-bin.zip  
# Verify package @TODO  
# Hawtio Managment Console  
EXPOSE 8161  
# Artemis | CORE,MQTT,AMQP,HORNETQ,STOMP,OPENWIRE  
EXPOSE 61616  
# AMQP  
EXPOSE 5672  
# HORNETQ,STOMP  
EXPOSE 5445  
# MQTT  
EXPOSE 1883  
# STOMP  
EXPOSE 61613  
# Expose some outstanding folders  
VOLUME ["/var/lib/amq7/data"]  
VOLUME ["/var/lib/amq7/tmp"]  
VOLUME ["/var/lib/amq7/etc"]  
  
WORKDIR /var/lib/amq7/bin  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["/sbin/tini", "--", "docker-entrypoint.sh"]  
  
CMD ["amq7-server"]  


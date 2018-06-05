FROM openjdk:jdk-alpine  
  
RUN apk add --no-cache su-exec \  
&& apk add --update curl \  
&& apk add --update bash \  
&& rm -rf /var/cache/apk/*  
  
##########################################################  
# Install Nexus  
##########################################################  
ENV SONATYPE_WORK /sonatype-work  
ENV NEXUS_VERSION 2.13.0-01  
#RUN mkdir -p ${SONATYPE_WORK}  
#ADD nexus.xml /opt/sonatype-work/nexus/conf/nexus.xml  
RUN sh -c 'curl -L
http://download.sonatype.com/nexus/oss/nexus-${NEXUS_VERSION}-bundle.tar.gz |
tar xvz -C /' \  
&& mv /nexus-${NEXUS_VERSION} /sonatype-nexus  
RUN mv /sonatype-work /swrktmp && mv /swrktmp ${SONATYPE_WORK}  
RUN addgroup nexus \  
&& adduser -S -G nexus -u 1000 -h ${SONATYPE_WORK} nexus \  
&& chown -R nexus:nexus /sonatype-nexus \  
&& chown -R nexus:nexus ${SONATYPE_WORK}  
EXPOSE 8081  
VOLUME ${SONATYPE_WORK}  
WORKDIR /sonatype-nexus  
ENV CONTEXT_PATH /  
ENV MAX_HEAP 768m  
ENV MIN_HEAP 256m  
ENV JAVA_OPTS -server -Djava.net.preferIPv4Stack=true  
ENV LAUNCHER_CONF ./conf/jetty.xml ./conf/jetty-requestlog.xml  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT /entrypoint.sh


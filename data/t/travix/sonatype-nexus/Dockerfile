FROM travix/base-debian-jre8:latest  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV NEXUS_VERSION=2.14.4-03 \  
SONATYPE_WORK=/sonatype-work \  
USER_NAME=nexus \  
USER_ID=200 \  
GROUP_NAME=nexus \  
GROUP_ID=200  
# install sonatype nexus  
RUN groupadd -r -g $GROUP_ID $GROUP_NAME \  
&& useradd -r -g $GROUP_NAME -u $USER_ID -d $SONATYPE_WORK $USER_NAME \  
&& mkdir -p /opt/sonatype/nexus $SONATYPE_WORK \  
&& chown -R ${USER_NAME}:${GROUP_NAME} ${SONATYPE_WORK} \  
&& curl --fail --location --retry 3
https://download.sonatype.com/nexus/professional-bundle/nexus-
professional-${NEXUS_VERSION}-bundle.tar.gz \  
| gunzip \  
| tar x -C /tmp nexus-professional-${NEXUS_VERSION} \  
&& mv /tmp/nexus-professional-${NEXUS_VERSION}/* /opt/sonatype/nexus/ \  
&& rm -rf /tmp/nexus-professional-${NEXUS_VERSION}  
  
# runtime environment variables  
ENV CONTEXT_PATH=/ \  
MAX_HEAP=768m \  
MIN_HEAP=256m \  
JAVA_OPTS="-server -Djava.net.preferIPv4Stack=true" \  
LAUNCHER_CONF="./conf/jetty.xml ./conf/jetty-requestlog.xml"  
EXPOSE 8081  
WORKDIR /opt/sonatype/nexus  
  
CMD groupmod -g ${GROUP_ID} ${GROUP_NAME}; \  
usermod -g ${GROUP_ID} -u ${USER_ID} ${USER_NAME}; \  
chown -R ${USER_NAME}:${GROUP_NAME} ${SONATYPE_WORK}; \  
/bin/su - ${USER_NAME} -c "cd /opt/sonatype/nexus && java -Dnexus-
work=${SONATYPE_WORK} -Dnexus-webapp-context-path=${CONTEXT_PATH}
-Xms${MIN_HEAP} -Xmx${MAX_HEAP} -cp 'conf/:lib/*' ${JAVA_OPTS}
org.sonatype.nexus.bootstrap.Launcher ${LAUNCHER_CONF}"  


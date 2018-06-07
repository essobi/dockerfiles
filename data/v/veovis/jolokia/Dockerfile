FROM jetty:alpine  
  
ARG JOLOKIA_VERSION=1.3.7  
ARG
JOLOKIA_ARCHIVE=https://github.com/rhuss/jolokia/releases/download/v${JOLOKIA_VERSION}/jolokia-${JOLOKIA_VERSION}-bin.tar.gz  
ENV JOLOKIA_HOME /opt/jolokia  
  
USER root  
# installing required packages and configuring the system  
RUN apk add \--no-cache libressl su-exec && \  
mkdir /opt  
  
# installing spark  
RUN wget -O - "$JOLOKIA_ARCHIVE" | tar -xz -C /tmp && \  
mv /tmp/jolokia-* "$JOLOKIA_HOME" && \  
chown -R root:root "$JOLOKIA_HOME" && \  
chmod u=rwX,go=rX "$JOLOKIA_HOME" && \  
cp /opt/jolokia/agents/jolokia.war /var/lib/jetty/webapps/  
  
COPY docker-entrypoint.sh /docker-entrypoint0.sh  
  
ENTRYPOINT [ "/docker-entrypoint0.sh" ]  
CMD ["java","-jar","/usr/local/jetty/start.jar"]


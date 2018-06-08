FROM openjdk:8  
MAINTAINER Tobias Larscheid <tobias.larscheid@de.ibm.com>  
  
ADD entrypoint.sh entrypoint.sh  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
USER root  
RUN chmod +x entrypoint.sh  
  
# Install WebSphere Liberty  
ENV LIBERTY_VERSION 16.0.0_02  
ARG LIBERTY_URL  
ARG DOWNLOAD_OPTIONS=""  
RUN LIBERTY_URL=${LIBERTY_URL:-$(wget -q -O -
https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/downloads/wlp/index.yml
| grep $LIBERTY_VERSION -A 6 | sed -n 's/\s*kernel:\s//p' | tr -d '\r' )} \  
&& wget $DOWNLOAD_OPTIONS $LIBERTY_URL -U UA-IBM-WebSphere-Liberty-Docker -O
/tmp/wlp.zip \  
&& unzip -q /tmp/wlp.zip -d /opt/ibm \  
&& rm /tmp/wlp.zip  
ENV PATH=/opt/ibm/wlp/bin:$PATH  
  
# Set Path Shortcuts  
ENV LOG_DIR=/logs \  
WLP_OUTPUT_DIR=/opt/ibm/wlp/output  
RUN mkdir /logs \  
&& ln -s $WLP_OUTPUT_DIR/defaultServer /output \  
&& ln -s /opt/ibm/wlp/usr/servers/defaultServer /config  
  
# Configure WebSphere Liberty  
RUN /opt/ibm/wlp/bin/server create \  
&& rm -rf $WLP_OUTPUT_DIR/.classCache /output/workarea  
COPY docker-server /opt/ibm/docker/  
  
EXPOSE 9080 9443  
ARG REPOSITORIES_PROPERTIES=""  
RUN if [ ! -z $REPOSITORIES_PROPERTIES ]; then echo $REPOSITORIES_PROPERTIES >
/opt/ibm/wlp/etc/repositories.properties; fi \  
&& installUtility install --acceptLicense collectiveMember-1.0 monitor-1.0
webCache-1.0 ldapRegistry-3.0 appSecurity-2.0 localConnector-1.0
restConnector-1.0 ssl-1.0 requestTiming-1.0 sessionDatabase-1.0 \  
webProfile-7.0 javaee-7.0\  
&& if [ ! -z $REPOSITORIES_PROPERTIES ] ; then rm
/opt/ibm/wlp/etc/repositories.properties; fi \  
&& rm -rf /output/workarea /output/logs  
  
CMD ./entrypoint.sh


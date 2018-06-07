FROM openjdk:alpine  
MAINTAINER Michael Edgar <michael@xlate.io>  
  
ENV INSTALL_DIR /opt  
ENV KARAF_VERSION 4.0.10  
ENV KARAF_BASE ${INSTALL_DIR}/karaf  
  
RUN apk add --no-cache bash gawk sed grep bc coreutils unzip curl \  
&& curl -o apache-karaf-${KARAF_VERSION}.zip -L
http://archive.apache.org/dist/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.zip \  
&& unzip -q apache-karaf-${KARAF_VERSION}.zip -d /opt/ \  
&& ln -s /opt/apache-karaf-${KARAF_VERSION} ${KARAF_BASE} \  
&& rm apache-karaf-${KARAF_VERSION}.zip \  
&& sed -i 's/^\\(.*rootLogger.*\\)out/\1stdout/'
${KARAF_BASE}/etc/org.ops4j.pax.logging.cfg  
  
VOLUME [ "${KARAF_BASE}/data" ]  
  
# Due to bug described here [ https://issues.apache.org/jira/browse/KARAF-4771
] it is necessary to  
# remove the instance.properties file when starting the container.  
ENTRYPOINT rm -f ${KARAF_BASE}/instances/instance.properties &&
${KARAF_BASE}/bin/karaf server  
EXPOSE 8181 8101  


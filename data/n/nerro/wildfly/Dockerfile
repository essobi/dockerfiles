FROM nerro/java:8u131-server-jre  
  
# configuration variables  
ENV WILDFLY_VERSION=11.0.0.Final \  
WILDFLY_SHA1=0e89fe0860a87bfd6b09379ee38d743642edfcfb \  
LAUNCH_JBOSS_IN_BACKGROUND=true  
  
RUN wget --output-document wildfly-${WILDFLY_VERSION}.tar.gz
http://download.jboss.org/wildfly/${WILDFLY_VERSION}/wildfly-${WILDFLY_VERSION}.tar.gz
\  
&& sha1sum wildfly-${WILDFLY_VERSION}.tar.gz | grep $WILDFLY_SHA1 \  
&& mkdir -p /opt/wildfly \  
&& tar -xzf wildfly-${WILDFLY_VERSION}.tar.gz -C /opt/wildfly --strip-
components=1 \  
&& rm -rf /opt/wildfly/docs \  
&& rm wildfly-${WILDFLY_VERSION}.tar.gz \  
  
&& groupadd -r wildfly --gid=999 && useradd -s /usr/sbin/nologin -r -g wildfly
--uid=999 wildfly \  
&& mkdir -p /opt/wildfly/standalone/log \  
&& chown -R wildfly:wildfly /opt/wildfly \  
  
&& wget -O /usr/local/bin/gosu
https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 \  
&& chmod +x /usr/local/bin/gosu  
  
VOLUME ["/opt/wildfly/standalone/deployments"]  
  
EXPOSE 8080 9990  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["wildfly"]  


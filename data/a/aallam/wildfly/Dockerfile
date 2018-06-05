FROM aallam/oracle-java:8  
MAINTAINER aallam  
  
WORKDIR /tmp  
  
COPY wildfly-10.1.0.Final.tar.gz.sha1 .  
  
RUN groupadd -r jboss -g 1000 && \  
useradd -u 1000 -r -g jboss -m -d /opt/jboss -s /sbin/nologin -c "JBoss user"
jboss && \  
chmod 755 /opt/jboss && \  
chown jboss:jboss wildfly-10.1.0.Final.tar.gz.sha1  
  
USER jboss  
  
ENV JBOSS_HOME /opt/jboss/wildfly-10  
RUN wget
http://download.jboss.org/wildfly/10.1.0.Final/wildfly-10.1.0.Final.tar.gz &&
\  
sha1sum -c wildfly-10.1.0.Final.tar.gz.sha1 && \  
tar xf wildfly-10.1.0.Final.tar.gz && \  
mv wildfly-10.1.0.Final $JBOSS_HOME && \  
rm wildfly-10.1.0.Final.tar.gz* && \  
cd $JBOSS_HOME/standalone/configuration/ && \  
sed -i 's/<core-environment>/<core-environment node-identifier="wildfly10">/g'
standalone.xml  
  
WORKDIR /  
  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
EXPOSE 8080  
CMD ["/opt/jboss/wildfly-10/bin/standalone.sh", "-b", "0.0.0.0"]  


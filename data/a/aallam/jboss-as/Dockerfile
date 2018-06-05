FROM aallam/oracle-java:7  
MAINTAINER aallam  
  
WORKDIR /tmp  
  
COPY jboss-as-7.1.1.Final.tar.gz.sha1 .  
  
RUN groupadd -r jboss -g 1000 && \  
useradd -u 1000 -r -g jboss -m -d /opt/jboss -s /sbin/nologin -c "JBoss user"
jboss && \  
chmod 755 /opt/jboss && \  
chown jboss:jboss jboss-as-7.1.1.Final.tar.gz.sha1  
  
USER jboss  
  
ENV JBOSS_HOME /opt/jboss/jboss-as  
  
RUN wget http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-
as-7.1.1.Final.tar.gz && \  
sha1sum -c jboss-as-7.1.1.Final.tar.gz.sha1 && \  
tar xf jboss-as-7.1.1.Final.tar.gz && \  
mv jboss-as-7.1.1.Final $JBOSS_HOME && \  
rm jboss-as-7.1.1.Final.tar.gz*  
  
WORKDIR /  
  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
EXPOSE 8080  
CMD ["/opt/jboss/jboss-as/bin/standalone.sh", "-b", "0.0.0.0"]  


FROM java:openjdk-7-jdk  
MAINTAINER hauke.mettendorf & thomas.steinbach @ iteratec.de  
  
ENV ITERAPLAN_URL https://www.iteraplan.de/downloads/iteraplan-lite-
bundle-5.2.0.zip  
ENV ITERAPLAN_HOME /opt/iteraplan  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# Add user  
RUN useradd iteraplan -M -f 0  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y unzip wget supervisor netcat && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN cd /tmp && \  
wget $ITERAPLAN_URL -O iteraplan.zip && \  
cd /tmp && \  
unzip -q iteraplan.zip && \  
mv /tmp/iteraplan* /opt/ && \  
cd /opt/iteraplan && \  
ln -s apache-tomcat-* tomcat && \  
rm /opt/iteraplan.zip && \  
rm -rf /tmp/*  
  
COPY config/tomcat-users.xml /opt/iteraplan/tomcat/conf/tomcat-users.xml  
COPY config/probe-2.4.0/probe.war /opt/iteraplan/tomcat/webapps/probe.war  
  
# Copy iteraplan to ROOT context  
RUN rm -rf /opt/iteraplan/tomcat/webapps/ROOT && \  
mv /opt/iteraplan/tomcat/webapps/iteraplan /opt/iteraplan/tomcat/webapps/ROOT  
  
RUN (chmod a+x /opt/iteraplan/*.sh && \  
chmod a+x /opt/iteraplan/tomcat/bin/*.sh)  
  
RUN chown -R iteraplan:iteraplan /opt/iteraplan  
  
# Configure statsd_status_reporter  
RUN mkdir -p /scripts  
  
# Copy statsd_status_reporter  
COPY config/statsd_status_reporter /scripts/statsd_status_reporter  
  
# Set permissions for reporter  
RUN chmod a+x /scripts/statsd_status_reporter  
  
# Configure supervisor  
COPY config/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
COPY config/supervisor/hsqldb.conf /etc/supervisor/conf.d/hsqldb.conf  
COPY config/supervisor/tomcat.conf /etc/supervisor/conf.d/tomcat.conf  
COPY config/supervisor/statsd_status_reporter.conf
/etc/supervisor/conf.d/statsd_status_reporter.conf  
  
# Volumes  
VOLUME /opt/iteraplan/hsqldb/data  
VOLUME /opt/iteraplan/tomcat/logs  
VOLUME /var/log/supervisor  
  
# Ports  
EXPOSE 8080  
EXPOSE 8009  
EXPOSE 8005  
EXPOSE 9001  
CMD /usr/bin/supervisord -n  


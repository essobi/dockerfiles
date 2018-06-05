FROM java:8-jre  
  
EXPOSE 61613 61614 61616  
ENV STOMP_PASSWORD=marionette \  
ACTIVEMQ_VERSION=5.14.3 \  
ACTIVEMQ_HOME=/opt/activemq  
  
ENV ACTIVEMQ=apache-activemq-$ACTIVEMQ_VERSION  
  
RUN apt-get update \  
&& apt-get install locales-all pwgen \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install puppet-agent  
ENV RELEASE jessie  
RUN apt-get update \  
&& apt-get install -y curl locales-all \  
&& curl -O http://apt.puppetlabs.com/puppetlabs-release-pc1-${RELEASE}.deb \  
&& dpkg -i puppetlabs-release-pc1-${RELEASE}.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y puppet-agent \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN \  
curl -O http://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-
bin.tar.gz && \  
mkdir -p /opt && \  
tar xf $ACTIVEMQ-bin.tar.gz -C /opt/ && \  
rm $ACTIVEMQ-bin.tar.gz && \  
mv /opt/$ACTIVEMQ $ACTIVEMQ_HOME && \  
useradd -r -M -d $ACTIVEMQ_HOME activemq && \  
chown activemq:activemq $ACTIVEMQ_HOME -R  
  
COPY activemq.xml $ACTIVEMQ_HOME/conf/activemq.xml  
COPY log4j.properties $ACTIVEMQ_HOME/conf/log4j.properties  
  
RUN chown activemq.activemq $ACTIVEMQ_HOME/conf/activemq.xml
$ACTIVEMQ_HOME/conf/log4j.properties  
  
USER activemq  
  
# Configure entrypoint  
COPY /docker-entrypoint.sh /  
COPY /docker-entrypoint.d/* /docker-entrypoint.d/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD [ "/opt/activemq/bin/activemq", "console" ]  


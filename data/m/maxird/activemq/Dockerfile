FROM maxird/java:7-8  
RUN export VERSION=5.15.3 && \  
cd /opt && \  
wget -q http://www.us.apache.org/dist/activemq/${VERSION}/apache-
activemq-${VERSION}-bin.tar.gz && \  
tar xf apache-activemq-${VERSION}-bin.tar.gz -C /opt/ && \  
rm apache-activemq-${VERSION}-bin.tar.gz && \  
ln -s apache-activemq-${VERSION} activemq && \  
echo 'export PATH=$PATH:/opt/activemq/bin' > /etc/profile.d/activemq.sh  
  
EXPOSE 1883 5672 8161 61613 61614 61616  
CMD ["/opt/activemq/bin/activemq", "console"]  


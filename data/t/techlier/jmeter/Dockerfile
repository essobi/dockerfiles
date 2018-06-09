FROM java:8-jre-alpine  
  
MAINTAINER Kazuhide Okamura <okamura@techlier.jp>  
  
ENV JMETER_VERSION 3.0  
ENV JMETER_HOME /opt/apache-jmeter-$JMETER_VERSION  
ENV JMETER_WORK /var/data/jmeter  
ENV PATH $JMETER_HOME/bin:$PATH  
  
RUN mkdir /opt  
  
# Install and configure Jmeter  
RUN \  
wget -q -O /tmp/jmeter.tgz
http://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz && \  
tar -xzf /tmp/jmeter.tgz --directory=/opt && \  
rm -f /tmp/jmeter.tgz  
  
RUN mkdir -p $JMETER_WORK  
WORKDIR $JMETER_WORK  
  
EXPOSE 1099  
CMD ["jmeter-server"]  


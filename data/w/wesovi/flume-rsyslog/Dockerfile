FROM dockerfile/java:oracle-java8  
MAINTAINER Iván Corrales Solera <developer@wesovi.com>  
  
# Defining variables  
ENV FLUME_VERSION 1.5.2  
ENV LUCENE_VERSION 4.10.3  
ENV ES_VERSION 1.4.4  
# Install Flume  
ADD http://mirror.nus.edu.sg/apache/flume/$FLUME_VERSION/apache-
flume-$FLUME_VERSION-bin.tar.gz /tmp/apache-flume-$FLUME_VERSION-bin.tar.gz  
RUN cd /tmp && tar -zvxf apache-flume-$FLUME_VERSION-bin.tar.gz -C /opt && mv
/opt/apache-flume-$FLUME_VERSION-bin /opt/flume  
  
#Copying required libraries to get Flume working with Elasticsearch  
ADD
http://www.eu.apache.org/dist/lucene/java/$LUCENE_VERSION/lucene-$LUCENE_VERSION.zip
/tmp/lucene-$LUCENE_VERSION.zip  
RUN cd /tmp && unzip /tmp/lucene-$LUCENE_VERSION.zip && mv
/tmp/lucene-$LUCENE_VERSION/**/*.jar /opt/flume/lib/  
  
ADD
http://jcenter.bintray.com/org/elasticsearch/elasticsearch/$ES_VERSION/elasticsearch-$ES_VERSION.jar
/opt/flume/lib/elasticsearch-$ES_VERSION.jar  
ADD http://central.maven.org/maven2/org/kitesdk/kite-morphlines-
core/1.0.0/kite-morphlines-core-1.0.0.jar /opt/flume/lib/kite-morphlines-
core-1.0.0.jar  
ADD http://central.maven.org/maven2/com/codahale/metrics/metrics-
core/3.0.2/metrics-core-3.0.2.jar /opt/flume/lib/metrics-core-3.0.2.jar  
ADD http://central.maven.org/maven2/com/codahale/metrics/metrics-
healthchecks/3.0.2/metrics-healthchecks-3.0.2.jar /opt/flume/lib/metrics-
healthchecks-3.0.2.jar  
ADD http://central.maven.org/maven2/com/typesafe/config/1.0.2/config-1.0.2.jar
/opt/flume/lib/config-1.0.2.jar  
  
#Copying resources  
RUN mkdir -p /opt/flume/agent  
COPY config/flume-env.sh /opt/flume/conf/flume-env.sh  
COPY agent/flume-ripple-flow-agent.properties /opt/flume/agent/flume-ripple-
flow-agent.properties  
COPY agent/flume-global-agent.properties /opt/flume/agent/flume-global-
agent.properties  
COPY config/morphline.conf /opt/flume/conf/morphline.conf  
  
#Temporary solution since agent configurations do not load env variables  
#Custom script to run agent.  
COPY bin/run-agents.sh /opt/run-agents.sh  
RUN chmod +x /opt/run-agents.sh  
  
#Install rsyslog centralized syslog server  
RUN apt-get update -q  
RUN apt-get install -y rsyslog  
  
#Configure rsyslogsserver  
COPY config/rsyslog.conf /etc/rsyslog.conf  
COPY config/50-default.conf /etc/rsyslog.d/50-default.conf  
  
#This directory will host the received remote logs  
RUN mkdir -p /var/log/hosts  
  
# supervisor installation &&  
# create directory for child images to store configuration in  
RUN apt-get -y install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
# supervisor base configuration  
COPY config/supervisor.conf /etc/supervisor.conf  
  
EXPOSE 10514  
EXPOSE 1514  
VOLUME /opt/flume/agent  
VOLUME /dev  
VOLUME /var/log  
VOLUME /var/flume/logs  
  
# default command  
CMD ["supervisord", "-c", "/etc/supervisor.conf"]  


FROM centos:7  
MAINTAINER infiniting222@gmail.com  
  
ENV FLUME_HOME=/flume/apache-flume-1.8.0-bin \  
FLUME_CONF=/flume/apache-flume-1.8.0-bin/conf \  
JAVA_HOME=/usr/lib/jvm/jre-openjdk \  
CLASSPATH=/flume/apache-flume-1.8.0-bin/lib/*  
  
  
RUN yum install java-1.8.0-openjdk.x86_64 -y && \  
mkdir -p /flume/apache-flume-1.8.0-bin  
  
ADD apache-flume-1.8.0-bin /flume/apache-flume-1.8.0-bin  
ADD entry.sh /  
  
RUN ln -sf /flume/apache-flume-1.8.0-bin/bin/flume-ng /usr/bin/flume-ng && \  
ln -sf /entry.sh /usr/bin/entry.sh  
  
CMD ["entry.sh"]


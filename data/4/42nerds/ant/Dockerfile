FROM 42nerds/java:7  
MAINTAINER 42nerds - Inh. Julian Kaffke <info@42nerds.com>  
  
ENV ANT_VERSION 1.9.6  
  
RUN cd && wget -q
http://mirror.serversupportforum.de/apache//ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /opt/ant && \  
rm -f apache-ant-${ANT_VERSION}-bin.tar.gz  
  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:/opt/ant/bin  


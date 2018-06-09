FROM ubuntu:14.04  
MAINTAINER Paul Velez "paul@relayrides.com"  
# Install java  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-
set-selections  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -y  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update -y && \  
apt-get install -y oracle-java8-installer \  
oracle-java8-set-default \  
tar \  
wget  
  
ENV TEAMCITY_VERSION 9.1.6  
RUN mkdir -p /opt && \  
wget -nv
http://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.tar.gz -O
/opt/TeamCity-$TEAMCITY_VERSION.tar.gz && \  
tar -C /opt --extract --file /opt/TeamCity-$TEAMCITY_VERSION.tar.gz && \  
rm -f /opt/TeamCity-$TEAMCITY_VERSION.tar.gz  
  
# Enable the correct Valve when running behind a proxy  
RUN sed -i -e "s/\\.*<\/Host>.*$/<Valve
className=\"org.apache.catalina.valves.RemoteIpValve\"
protocolHeader=\"x-forwarded-proto\" \/><\/Host>/"
/opt/TeamCity/conf/server.xml  
  
VOLUME ["/data/teamcity"]  
# Expose the Teamcity port  
EXPOSE 8111  
# TEAMCITY_DATA_PATH path to TeamCity data directory  
# TEAMCITY_SERVER_MEM_OPTS server memory options (JVM options)  
# TEAMCITY_SERVER_OPTS additional server JVM options  
# TEAMCITY_PREPARE_SCRIPT name of a script to execute before start/stop  
ENV TEAMCITY_DATA_PATH /data/teamcity  
ENV TEAMCITY_SERVER_MEM_OPTS "-Xms1024m -Xmx3048m
-XX:ReservedCodeCacheSize=350m"  
WORKDIR /opt/TeamCity  
CMD ["/opt/TeamCity/bin/teamcity-server.sh", "run"]  


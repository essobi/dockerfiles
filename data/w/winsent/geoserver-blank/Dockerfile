FROM ubuntu:trusty  
  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV GEOSERVER_HOME /opt/geoserver  
ENV JAVA_HOME /usr  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/lib/jni:/usr/share/java  
  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN dpkg-divert --local --rename --add /sbin/initctl  
  
# Install packages  
RUN \  
apt-get -y update --fix-missing && \  
apt-get -y install unzip software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get -y update && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
rm -rf /tmp/* /var/tmp/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV GEOSERVER_VERSION 2.12.0  
  
# Get GeoServer  
RUN wget -c
http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/geoserver-$GEOSERVER_VERSION-
bin.zip -O ~/geoserver.zip &&\  
unzip ~/geoserver.zip -d /opt && mv -v /opt/geoserver* /opt/geoserver && \  
rm ~/geoserver.zip  
  
# Expose GeoServer's default port  
EXPOSE 8080  
CMD ["/opt/geoserver/bin/startup.sh"]  


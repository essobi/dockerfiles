FROM ibmjava:8-sdk  
  
MAINTAINER rjrivero  
  
# Install dependencies.  
#  
# - xvfb to support headless reports  
#  
# Oracle java no longer used, but link kept here for reference:  
# http://www.webupd8.org/2012/01/install-oracle-java-jdk-7-in-ubuntu-via.html  
#  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \  
apt-get install -y xvfb  
  
# Set environment variables for Pentaho  
ENV JAVA_HOME "/opt/ibm/java"  
ENV PENTAHO_JAVA_HOME "/opt/ibm/java"  
ENV PENTAHO_JAVA "/opt/ibm/java/bin/java"  
# Support software versions  
# Get this version from https://dev.mysql.com/downloads/connector/j/  
ENV MYSQL_CONN_VERSION 5.1.45  
# Get this version from https://jdbc.postgresql.org/download.html  
ENV PGSQL_CONN_VERSION 42.2.1  
# Get this version from https://apr.apache.org/download.cgi  
ENV APR_VERSION 1.6.3  
# Get this version from https://tomcat.apache.org/download-native.cgi  
ENV TCN_VERSION 1.1.34  
# Get this version from https://logging.apache.org/log4j/extras/  
ENV LOG4J_EXTRAS_VERSION 1.2.17  
# C3P0 connection pool from https://sourceforge.net/projects/c3p0/  
ENV C3P0_VERSION 0.9.5.2  
ENV JAVA_VERSION 8  
# Install libtcnative libraries and other dependencies  
ADD files/install.sh /opt/install.sh  
ADD files/opt /opt  
RUN /opt/install.sh && rm -f /opt/install.sh  
  
# Pentaho must be downloaded, uncompressed and mounted as a volume  
# in the path /opt/pentaho-server  
#  
# Pentaho can be downloaded from:  
# http://downloads.sourceforge.net/project/pentaho/Business Intelligence
Server/${PENTAHO_MAJOR}/pentaho-server-${PENTAHO_MINOR}.zip  
VOLUME /opt/pentaho-server  
WORKDIR /opt/pentaho-server  
  
# Pentaho port  
EXPOSE 8080  
# Change "start" with "run" in tomcat/bin/startup.sh so it runs in foreground  
CMD /opt/pentaho-server/start-pentaho.sh  
  


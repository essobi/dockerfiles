# Pentaho Business Analytics 5.0  
#  
# VERSION 1.1  
FROM ubuntu:12.04  
MAINTAINER Johan Warlander, johan@snowflake.nu  
  
# Make sure package repository is up to date  
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install some basic utilities  
RUN apt-get install -y curl git zip  
  
# Add the Web Upd8 Oracle Java 7 repository  
RUN apt-get install -y python-software-properties  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update  
  
# Install Oracle Java 7  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java7-installer  
  
# Set up Pentaho user + directory  
# - must have home directory where Pentaho can store config etc  
# - also set up installation directory with ownership  
RUN useradd -m pentaho  
RUN mkdir /opt/pentaho  
RUN chown pentaho:pentaho /opt/pentaho  
  
# Install Pentaho Business Analytics  
RUN su -c "curl -L
http://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/5.0.1-stable/biserver-
ce-5.0.1-stable.zip/download -o /opt/pentaho/biserver-ce.zip" pentaho  
RUN su -c "unzip -q /opt/pentaho/biserver-ce.zip -d /opt/pentaho/" pentaho  
  
# Disable first-time startup prompt  
RUN rm /opt/pentaho/biserver-ce/promptuser.sh  
# Disable daemon mode for Tomcat  
RUN sed -i -e 's/\\(exec ".*"\\) start/\1 run/' /opt/pentaho/biserver-
ce/tomcat/bin/startup.sh  
  
# Set up runtime options  
EXPOSE 8080  
ENTRYPOINT ["/opt/pentaho/biserver-ce/start-pentaho.sh"]  
USER pentaho  


#  
# Ubuntu 14.04  
#  
# https://hub.docker.com/_/ubuntu/  
#  
# Pull base image.  
FROM uwitech/ohie-base  
  
USER root  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y git build-essential curl wget software-properties-common  
  
RUN apt-get install -y postgresql-client  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
#install openempi  
RUN mkdir sysnet  
RUN cd sysnet  
COPY openempi-3.3.0c /sysnet/openempi-3.3.0c  
RUN export OPENEMPI_HOME=/sysnet/openempi-3.3.0c  
RUN export CATALINA_BASE=/sysnet/openempi-3.3.0c  
  
# Install Tomcat  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.12  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
ENV CATALINA_HOME /sysnet/openempi-3.3.0c  
ENV PATH $CATALINA_HOME/bin:$PATH  
ENV OPENEMPI_HOME /sysnet/openempi-3.3.0c  
ENV PATH $OPENEMPI_HOME/bin:$PATH  
  
EXPOSE 8080  
RUN rm -r /sysnet/openempi-3.3.0c/webapps/ROOT/  
  
# Launch Tomcat  
WORKDIR /  
COPY /cmd.sh /cmd.sh  
RUN chmod +x /cmd.sh  
  
CMD /cmd.sh  
  


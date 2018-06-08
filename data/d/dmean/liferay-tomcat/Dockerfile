FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install java  
RUN \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee
-a /etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" |
tee -a /etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update  
  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
apt-get install -y oracle-java8-installer  
  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment  
  
# Install liferay  
## download  
RUN wget -O /tmp/liferay-portal-tomcat-6.2-ce-ga2-20140319114139101.zip \  
http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.2.1%20GA2/liferay-
portal-tomcat-6.2-ce-ga2-20140319114139101.zip  
  
## uncompress liferay bundle  
RUN apt-get install -y unzip  
RUN unzip /tmp/liferay-portal-tomcat-6.2-ce-ga2-20140319114139101.zip -d /opt  
RUN mv /opt/liferay-portal-6.2-ce-ga2 /opt/liferay-portal  
  
## install APR  
RUN apt-get install -y libtcnative-1  
RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/liferay-
portal/tomcat-7.0.42/lib  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Volumes  
VOLUME ["/var/liferay", "/opt/liferay-portal/deploy", "/opt/liferay-
portal/data"]  
  
# Configure liferay  
ENV JAVA_OPTS '-Dexternal-properties=/var/liferay/portal-ext.properties'  
# Ports  
EXPOSE 8080  
# EXEC  
ENTRYPOINT ["/opt/liferay-portal/tomcat-7.0.42/bin/catalina.sh"]  
CMD ["run"]  


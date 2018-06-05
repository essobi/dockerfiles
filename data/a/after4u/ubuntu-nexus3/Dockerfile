FROM after4u/ubuntu-jdk8:latest  
MAINTAINER Ken Huang <ken@after4u.com>  
  
RUN cd /tmp && \  
wget -O /tmp/nexus-bundle.tar.gz
http://download.sonatype.com/nexus/3/nexus-3.0.0-03-unix.tar.gz && \  
tar -zxf /tmp/nexus-bundle.tar.gz -C /usr/local && \  
mv /usr/local/nexus-3.0.0-* /usr/local/nexus && \  
mkdir -p /usr/local/sonatype-work/nexus/logs && \  
touch /usr/local/sonatype-work/nexus/logs/nexus.log && \  
rm /tmp/nexus-bundle.tar.gz && \  
useradd -m nexus && \  
chown -R nexus /usr/local/sonatype-work && \  
chown -R nexus /usr/local/nexus  
  
# generate SSL  
RUN mkdir /usr/local/nexus/etc/ssl && \  
cd /usr/local/nexus/etc/ssl && \  
keytool -genkey -alias tomcat -keyalg RSA -keystore keystore.jks -storepass
password -keypass password -validity 3650 -dname "CN=dtr.after4u.com,
OU=Docker, O=After4u, L=Auckland, S=Auckland, C=NZ"  
  
#ADD usr/local/nexus/etc/custom.properties
/usr/local/nexus/etc/custom.properties  
#ADD usr/local/nexus/etc/jetty-https.xml /usr/local/nexus/etc/jetty-https.xml  
ADD usr/local/nexus/etc/org.sonatype.nexus.cfg
/usr/local/nexus/etc/org.sonatype.nexus.cfg  
  
VOLUME /usr/local/sonatype-work/nexus  
VOLUME /usr/local/nexus/data  
  
ADD etc/supervisor.d/supervisord-nexus.conf /etc/supervisor.d/supervisord-
nexus.conf  
  
ADD start-nexus.sh /start-nexus.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 8081  
EXPOSE 8443  
EXPOSE 18443  
EXPOSE 18444  
#USER nexus  
WORKDIR /usr/local/nexus/bin


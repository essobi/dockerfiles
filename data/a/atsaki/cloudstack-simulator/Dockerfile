FROM ubuntu:14.04  
RUN echo 'mysql-server mysql-server/root_password password root' | debconf-
set-selections; \  
echo 'mysql-server mysql-server/root_password_again password root' | debconf-
set-selections; \  
apt-get -y update ; \  
apt-get install -qqy \  
wget \  
genisoimage \  
maven \  
openjdk-7-jdk \  
openssh-client \  
supervisor \  
mysql-server ; \  
apt-get clean all ; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN (/usr/bin/mysqld_safe &); sleep 5; mysqladmin -u root -proot password ''  
  
RUN wget https://github.com/apache/cloudstack/archive/4.5.2.tar.gz ; \  
tar xvfz 4.5.2.tar.gz ; \  
mv cloudstack-4.5.2/* /root ; \  
rm -frv 4.5.2.tar.gz cloudstack-4.5.2  
  
WORKDIR /root  
  
RUN mvn -Pdeveloper -Dsimulator -DskipTests clean install  
  
RUN (/usr/bin/mysqld_safe &); \  
sleep 3; \  
mvn -Pdeveloper -pl developer -Ddeploydb; \  
mvn -Pdeveloper -pl developer -Ddeploydb-simulator  
  
RUN sed -i -e 's/<param name="Threshold" value=".*"\/>/<param name="Threshold"
value="DEBUG"\/>/g' \  
-e 's/<param name="ConversionPattern" value="%-5p/<param name="ConversionPattern" value="%d{ISO8601} %-5p/' \  
/root/client/tomcatconf/log4j-cloud.xml.in  
  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 8080 8096  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  


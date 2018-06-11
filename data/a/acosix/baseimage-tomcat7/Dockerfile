FROM acosix/baseimage-jdk8:latest  
  
LABEL vendor="Acosix GmbH" \  
de.acosix.version="0.0.1-SNAPSHOT" \  
de.acosix.is-beta="" \  
de.acosix.is-production="" \  
de.acosix.release-date="2017-08-27" \  
de.acosix.maintainer="axel.faust@acosix.de"  
  
ENV JMX_RMI_PORT=5000  
  
EXPOSE 8080 8081 5000  
  
# unzip/zip in case some derived image needs to extract or include files
from/in WAR-files  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -q \  
&& apt-get upgrade -q -y -o Dpkg::Options::="--force-confdef" -o
Dpkg::Options::="--force-confold" \  
&& apt-get install -q -y -o Dpkg::Options::="--force-confdef" -o
Dpkg::Options::="--force-confold" \  
tomcat7 \  
libtcnative-1 \  
unzip \  
zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/tomcat7/webapps/ROOT  
# add prepared files that would be too awkward to handle via RUN / sed  
COPY server.xml users.xml initTomcat.sh startTomcat.sh tomcat-logrotate.d
/tmp/  
# apply our tomcat default configurations  
RUN cp /tmp/*.xml /etc/tomcat7/ \  
&& cp /tmp/tomcat-logrotate.d /etc/logrotate.d/tomcat7 \  
&& touch /var/lib/tomcat7/logs/.access-logrotate-dummy \  
&& rm /tmp/*.xml /tmp/tomcat-logrotate.d \  
&& chown root:tomcat7 /etc/tomcat7/server.xml /etc/tomcat7/tomcat-users.xml \  
&& chown -R tomcat7:tomcat7 /var/lib/tomcat7 /var/log/tomcat7 \  
&& chmod 640 /etc/tomcat7/server.xml /etc/tomcat7/tomcat-users.xml \  
&& sed -i 's/^handlers = .*/handlers = java.util.logging.ConsoleHandler/'
/etc/tomcat7/logging.properties \  
&& sed -i
's/\(common\\.loader=\\).*/\1${catalina.base}\/lib,${catalina.base}\/lib\/*.jar,${catalina.home}\/lib,${catalina.home}\/lib\/*.jar,${catalina.home}\/common\/classes,${catalina.home}\/common\/*.jar/'
/etc/tomcat7/catalina.properties \  
&& sed -i
's/\(shared\\.loader=\\).*/\1${catalina.base}\/shared\/classes,${catalina.base}\/shared\/*.jar/'
/etc/tomcat7/catalina.properties \  
&& mkdir -p /usr/share/tomcat7/common/classes
/usr/share/tomcat7/server/classes /var/lib/tomcat7/lib
/var/lib/tomcat7/shared/classes \  
&& sed -i 's/^JAVA_OPTS=.*/JAVA_OPTS="-Djava.awt.headless=true %JAVA_OPTS%"/'
/etc/default/tomcat7 \  
&& mkdir -p /etc/my_init.d \  
&& mv /tmp/initTomcat.sh /etc/my_init.d/20_initTomcat.sh \  
&& chmod +x /etc/my_init.d/20_initTomcat.sh \  
&& mkdir /etc/service/tomcat7 \  
&& mv /tmp/startTomcat.sh /etc/service/tomcat7/run \  
&& chmod +x /etc/service/tomcat7/run


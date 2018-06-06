FROM debian:jessie  
MAINTAINER Steve Hibit <sdhibit@gmail.com>  
  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Exclude docs and man pages  
ADD excludes /etc/dpkg/dpkg.cfg.d/excludes  
  
# Install Apt Packages  
RUN apt-get update && apt-get install -y \  
freerdp-x11 \  
gcc \  
libcairo2-dev \  
libfreerdp-dev \  
libossp-uuid-dev \  
libpango-1.0-0 \  
libpango1.0-dev \  
libpng12-dev \  
libpulse-dev \  
libssh-dev \  
libssh2-1 \  
libssh2-1-dev \  
libssl1.0.0 \  
libtelnet-dev \  
libvncserver-dev \  
libvorbis-dev \  
make \  
openjdk-7-jre-headless \  
supervisor \  
tomcat7 \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/groff \  
/usr/share/info \  
/usr/share/lintian \  
/usr/share/linda \  
/var/cache/man \  
&& (( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true ))
\  
&& (( find /usr/share/doc -empty|xargs rmdir || true ))  
  
ENV GUACAMOLE_VERSION 0.9.3  
ENV GUACAMOLE_HOME /etc/guacamole  
ENV TOMCAT_VERSION tomcat7  
ENV CATALINA_BASE /var/lib/tomcat7  
ENV CATALINA_HOME /usr/share/tomcat7  
ENV MYSQL_CONN_VERSION 5.1.34  
  
WORKDIR /tmp  
  
# Intall Guacamole Client and Server  
RUN wget
http://downloads.sourceforge.net/project/guacamole/current/source/guacamole-
server-${GUACAMOLE_VERSION}.tar.gz \  
&& wget
http://downloads.sourceforge.net/project/guacamole/current/binary/guacamole-${GUACAMOLE_VERSION}.war
\  
&& mkdir -p ${GUACAMOLE_HOME} \  
&& mkdir -p ${CATALINA_HOME}/.guacamole \  
&& mkdir -p /var/lib/guacamole/classpath \  
&& mv guacamole-${GUACAMOLE_VERSION}.war /var/lib/guacamole/guacamole.war \  
&& tar -xvzf guacamole-server-${GUACAMOLE_VERSION}.tar.gz --strip-components 1
\  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
&& ln -s /var/lib/guacamole/guacamole.war ${CATALINA_BASE}/webapps \  
&& ln -s ${GUACAMOLE_HOME}/guacamole.properties /usr/share/tomcat7/.guacamole
\  
&& rm -rf /tmp/*  
  
ADD ./config/* /etc/guacamole/  
ADD ./supervisor/supervisor.conf /etc/supervisor/  
ADD ./supervisor/guacd.sv.conf /etc/supervisor/conf.d/  
ADD ./supervisor/tomcat7.sv.conf /etc/supervisor/conf.d/  
  
# Add Extensions to Guacamole  
RUN wget
http://downloads.sourceforge.net/project/guacamole/current/extensions/guacamole-
auth-mysql-${GUACAMOLE_VERSION}.tar.gz \  
&& wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONN_VERSION}.tar.gz \  
&& wget
http://sourceforge.net/projects/guacamole/files/current/extensions/guacamole-
auth-ldap-${GUACAMOLE_VERSION}.tar.gz \  
&& wget
http://sourceforge.net/projects/guacamole/files/current/extensions/guacamole-
auth-noauth-${GUACAMOLE_VERSION}.tar.gz \  
&& tar -xvzf guacamole-auth-mysql-${GUACAMOLE_VERSION}.tar.gz \  
&& mv guacamole-auth-mysql-${GUACAMOLE_VERSION}/lib/*
/var/lib/guacamole/classpath/ \  
&& tar -xvzf mysql-connector-java-${MYSQL_CONN_VERSION}.tar.gz \  
&& mv mysql-connector-java-${MYSQL_CONN_VERSION}/mysql-connector-
java-${MYSQL_CONN_VERSION}-bin.jar /var/lib/guacamole/classpath/ \  
&& tar -xvzf guacamole-auth-ldap-${GUACAMOLE_VERSION}.tar.gz \  
&& mv guacamole-auth-ldap-${GUACAMOLE_VERSION}/lib/*
/var/lib/guacamole/classpath/ \  
&& tar -xvzf guacamole-auth-noauth-${GUACAMOLE_VERSION}.tar.gz \  
&& mv guacamole-auth-noauth-${GUACAMOLE_VERSION}/lib/*
/var/lib/guacamole/classpath/ \  
&& rm -rf /tmp/*  
  
# Enable AJP - http://stackoverflow.com/questions/24060950/delete-line-before-
and-after-found-pattern  
RUN sed -i '$!N;/<Connector port="8009" protocol="AJP\/1.3"
redirectPort="8443" \/>/{s/.*\n//p;$!N;d};P;D'
/etc/${TOMCAT_VERSION}/server.xml  
  
WORKDIR ${CATALINA_HOME}  
  
EXPOSE 8009  
EXPOSE 8080  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]  


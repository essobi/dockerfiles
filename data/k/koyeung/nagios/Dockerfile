# [Ubuntu
Quickstart](https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/quickstart-
ubuntu.html)  
FROM debian:jessie  
MAINTAINER King-On Yeung <koyeung@gmail.com>  
  
ENV NAGIOS_VERSION 4.1.1  
ENV NAGIOS_PLUGIN_VERSION 2.1.1  
ENV NAGIOS_USER nagios  
ENV NAGIOS_GROUP nagios  
ENV NAGIOS_CMDGROUP nagcmd  
  
#  
# Configurable when container is launched  
#  
# Web UI logon  
ENV NAGIOSADMIN_USER nagiosadmin  
ENV NAGIOSADMIN_PASS nagios  
  
ENV NAGIOSADMIN_EMAIL nagios@localhost  
  
# see /usr/share/zoneinfo for list of timezones  
# ENV TZ Asia/Hong_Kong  
ENV TZ Etc/UTC  
  
#  
# Non-configurable variables  
# to match default values of software packages  
#  
ENV NAGIOS_HOME /usr/local/nagios  
ENV NAGIOS_HTTPD_CONFDIR /etc/apache2/conf-available  
ENV APACHE_RUN_USER www-data  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Setup Required Packages  
RUN apt-get update && \  
apt-get install -y apt-utils && \  
apt-get install -y apache2 libapache2-mod-php5 build-essential libgd2-xpm-dev
unzip && \  
apt-get install -y postfix mailutils && \  
apt-get clean  
  
# Create Account Information  
RUN /usr/sbin/useradd -m -s /bin/bash ${NAGIOS_USER} && \  
/usr/sbin/groupadd ${NAGIOS_CMDGROUP} && \  
/usr/sbin/usermod -a -G ${NAGIOS_CMDGROUP} ${NAGIOS_USER} && \  
/usr/sbin/usermod -a -G ${NAGIOS_CMDGROUP} ${APACHE_RUN_USER}  
  
# Download Nagios and the Plugins  
ADD
https://assets.nagios.com/downloads/nagioscore/releases/nagios-${NAGIOS_VERSION}.tar.gz
/tmp/  
ADD http://www.nagios-plugins.org/download/nagios-
plugins-${NAGIOS_PLUGIN_VERSION}.tar.gz /tmp/  
  
# Compile, install Nagios, and web interface  
RUN cd /tmp && \  
tar zxf /tmp/nagios-${NAGIOS_VERSION}.tar.gz && \  
cd nagios-${NAGIOS_VERSION} && \  
./configure --with-command-group=${NAGIOS_CMDGROUP} \--with-httpd-
conf=${NAGIOS_HTTPD_CONFDIR} && \  
make all && \  
make install && \  
make install-init && \  
make install-config && \  
make install-commandmode && \  
make install-webconf && \  
cd /tmp && \  
rm -rf nagios-${NAGIOS_VERSION}  
  
# Enable web config  
RUN a2enconf nagios && \  
a2enmod cgi  
  
# Compile and install Nagios Plugins  
RUN cd /tmp && \  
tar zxf /tmp/nagios-plugins-${NAGIOS_PLUGIN_VERSION}.tar.gz && \  
cd nagios-plugins-${NAGIOS_PLUGIN_VERSION} && \  
./configure --with-nagios-user=${NAGIOS_USER} \--with-nagios-
group=${NAGIOS_GROUP} && \  
make && \  
make install && \  
cd /tmp && \  
rm -rf nagios-plugins-${NAGIOS_PLUGIN_VERSION}  
  
# patch: use /usr/bin/mail instead of /bin/mail  
RUN sed -i -e 's,/bin/mail,/usr/bin/mail,'
${NAGIOS_HOME}/etc/objects/commands.cfg  
  
# config test  
RUN /etc/init.d/nagios configtest  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80/tcp  
VOLUME ["${NAGIOS_HOME}/etc", "${NAGIOS_HOME}/var", "/var/log/apache2"]  


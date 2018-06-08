FROM ubuntu:14.04  
MAINTAINER Lyle Scott, III "lyle@digitalfoo.net"  
# Credits that helped buld this docker image::  
#
https://raymii.org/s/tutorials/Nagios_Core_4_Installation_on_Ubuntu_12.04.html  
# https://github.com/cpuguy83/docker-nagios  
ENV NAGIOS_VERSION 4.0.8  
ENV NAGIOSPLUGINS_VERSION 2.0.3  
ENV NRPE_VERSION 2.15  
ENV WORK_DIR /tmp  
  
ENV NAGIOS_HOME /opt/nagios  
ENV NAGIOS_USER nagios  
ENV NAGIOS_GROUP nagios  
ENV NAGIOS_CMDGROUP nagioscmd  
ENV NAGIOSADMIN_USER nagiosadmin  
ENV NAGIOSADMIN_PASS nagios  
ENV NAGIOS_WEB_DIR $NAGIOS_HOME/share  
  
ENV APACHE_RUN_USER nagios  
ENV APACHE_RUN_GROUP nagios  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVERNAME localhost  
ENV APACHE_SERVERALIAS docker.localhost  
ENV APACHE_ERROR_LOG /dev/stdout  
ENV APACHE_LOG_LEVEL error  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
#>> Install dependency packages.  
RUN apt-get update &&\  
apt-get install -q -y apache2 supervisor postfix libapache2-mod-php5 build-
essential libgd2-xpm-dev libssl-dev wget apache2-utils libnet-snmp-perl libpq5
libradius1 libsensors4 libsnmp-base libtalloc2 libtdb1 libwbclient0 samba-
common samba-common-bin smbclient snmp whois mrtg libmysqlclient15-dev libcgi-
pm-perl librrds-perl libgd-gd2-perl  
  
#>> Add users and such.  
RUN groupadd -g 3000 ${NAGIOS_GROUP}  
RUN groupadd -g 3001 ${NAGIOS_CMDGROUP}  
RUN useradd -u 3000 -g ${NAGIOS_GROUP} -G ${NAGIOS_CMDGROUP} -d ${NAGIOS_HOME}
-c 'Nagios Admin' ${NAGIOS_USER}  
RUN adduser www-data ${NAGIOS_CMDGROUP}  
  
#>> Install Nagios4  
RUN mkdir -p ${NAGIOS_HOME}/share/{stylesheets,images}  
RUN mkdir -p ${WORK_DIR}/nagios4 &&\  
cd ${WORK_DIR}/nagios4 &&\  
wget
http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-${NAGIOS_VERSION}.tar.gz
&&\  
tar -xf nagios-${NAGIOS_VERSION}.tar.gz &&\  
cd nagios-${NAGIOS_VERSION} &&\  
./configure \  
\--prefix=${NAGIOS_HOME} \  
\--with-nagios-user=${NAGIOS_USER} \  
\--with-nagios-group=${NAGIOS_GROUP} \  
\--with-command-user=${NAGIOS_USER} \  
\--with-command-group=${NAGIOS_CMDGROUP} &&\  
make all &&\  
make install && make install-config && make install-commandmode &&\  
/usr/bin/install -c -m 644 sample-config/httpd.conf /etc/apache2/conf-
available/nagios.conf &&\  
ln -s /etc/apache2/conf-available/nagios.conf /etc/apache2/conf-
enabled/nagios.conf  
  
#>> Install Nagios Plugins  
RUN mkdir -p ${WORK_DIR}/nagios-plugins &&\  
cd ${WORK_DIR}/nagios-plugins &&\  
wget https://www.nagios-plugins.org/download/nagios-
plugins-${NAGIOSPLUGINS_VERSION}.tar.gz &&\  
tar -xf nagios-plugins-${NAGIOSPLUGINS_VERSION}.tar.gz &&\  
cd nagios-plugins-${NAGIOSPLUGINS_VERSION} &&\  
./configure \  
\--prefix=${NAGIOS_HOME} \  
\--with-nagios-user=${NAGIOS_USER} \  
\--with-nagios-group=${NAGIOS_GROUP} \  
\--with-openssl=/usr/bin/openssl \  
\--enable-perl-modules \  
\--enable-libtap &&\  
make &&\  
make install  
  
#>> Install NRPE  
RUN mkdir -p ${WORK_DIR}/nrpe &&\  
cd ${WORK_DIR}/nrpe &&\  
wget
http://kent.dl.sourceforge.net/project/nagios/nrpe-2.x/nrpe-${NRPE_VERSION}/nrpe-${NRPE_VERSION}.tar.gz
&&\  
tar -xf nrpe-${NRPE_VERSION}.tar.gz &&\  
cd nrpe-${NRPE_VERSION} &&\  
./configure \  
\--prefix=${NAGIOS_HOME} \  
\--with-ssl=/usr/bin/openssl \  
\--with-ssl-lib=/usr/lib/x86_64-linux-gnu &&\  
make &&\  
make install  
  
#>> Install and Configure Apache  
RUN sed -i "s|\\(^ErrorLog \\).*|\1${APACHE_ERROR_LOG}|"
/etc/apache2/apache2.conf &&\  
sed -i "s|\\(^LogLevel \\).*|\1${APACHE_LOG_LEVEL}|" /etc/apache2/apache2.conf  
# Enable SSL module.  
RUN a2enmod ssl  
# Generate a SSL key for HTTPS access to Nagios web service.  
ADD nagios.pem /etc/apache2/ssl/nagios.pem  
ADD nagios.key /etc/apache2/ssl/nagios.key  
# Create a place for the Nagios HTTP docs to live.  
RUN mkdir -p ${NAGIOS_WEB_DIR}  
RUN chown www-data:www-data ${NAGIOS_WEB_DIR}  
RUN a2enmod cgi  
RUN a2dissite 000-default  
ADD vhost.conf /etc/apache2/sites-available/nagios.conf  
RUN a2ensite nagios  
RUN htpasswd -c -b -s ${NAGIOS_HOME}/etc/htpasswd.users ${NAGIOSADMIN_USER}
${NAGIOSADMIN_PASS} &&\  
chown -R nagios.nagios ${NAGIOS_HOME}/etc/htpasswd.users  
  
#>> Copy over the supervisord config.  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#>> Cleanup  
RUN apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
rm -rf /tmp/* /var/lib/apt/lists/*  
  
EXPOSE 443  
#ADD ensure_env /etc/init.d/ensure_env  
#CMD ["su", "-c", "/etc/init.d/ensure_env ; /usr/bin/supervisord"]  
CMD ["/usr/bin/supervisord"]  


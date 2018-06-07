FROM ubuntu:16.04  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# ---- package version  
  
ENV NAGIOS_CORE_VERSION 4.3.4  
ENV NAGIOS_CORE_ARCHIVE
https://github.com/NagiosEnterprises/nagioscore/archive/nagios-${NAGIOS_CORE_VERSION}.tar.gz  
  
ENV NAGIOS_NRPE_VERSION 3.2.1  
ENV NAGIOS_NRPE_ARCHIVE
https://github.com/NagiosEnterprises/nrpe/archive/nrpe-${NAGIOS_NRPE_VERSION}.tar.gz  
  
ENV NAGIOS_PLUGINS_VERSION 2.2.1  
ENV NAGIOS_PLUGINS_ARCHIVE https://nagios-plugins.org/download/nagios-
plugins-${NAGIOS_PLUGINS_VERSION}.tar.gz  
  
# ---- environment variables  
  
ENV NAGIOS_USER nagios  
ENV NAGIOS_GROUP nagios  
  
ENV NAGIOS_WEB_USER nagiosadmin  
ENV NAGIOS_WEB_PASS adminpass  
  
ENV NAGIOS_HOME /opt/nagios  
  
# ---- ensure user existence before provision  
  
RUN groupadd ${NAGIOS_GROUP} && \  
useradd \--system -d ${NAGIOS_HOME} -g ${NAGIOS_GROUP} ${NAGIOS_USER}  
  
# ---- basic requirements  
  
RUN apt update && \  
apt install -y --no-install-recommends \  
apache2 \  
apache2-utils \  
autoconf \  
dnsutils \  
fping \  
gcc \  
iputils-ping \  
libapache2-mod-php7.0 \  
libc6 \  
libgd-dev \  
libgd2-xpm-dev \  
libmcrypt-dev \  
libssl-dev \  
make \  
openssl \  
php7.0-cli \  
php7.0-gd \  
snmp \  
supervisor \  
unzip \  
wget  
  
# ---- nagios core  
  
RUN mkdir -p /tmp/nagios && \  
wget \--no-check-certificate ${NAGIOS_CORE_ARCHIVE} \  
-qO /tmp/nagioscore.tar.gz && \  
tar \--strip 1 -zxf /tmp/nagioscore.tar.gz -C /tmp/nagios && \  
cd /tmp/nagios && \  
./configure \  
\--prefix=${NAGIOS_HOME} \  
\--exec-prefix=${NAGIOS_HOME} \  
\--with-httpd-conf=/etc/apache2/conf-available \  
\--with-nagios-user=${NAGIOS_USER} \  
\--with-nagios-group=${NAGIOS_GROUP} && \  
make all && \  
make install && \  
make install-init && \  
make install-config && \  
make install-commandmode && \  
make install-webconf && \  
make clean && \  
cd ~ && \  
rm -rf /tmp/nagios && \  
rm -rf /tmp/nagioscore.tar.gz && \  
/opt/nagios/bin/nagios -v /opt/nagios/etc/nagios.cfg  
  
# ---- nagios plugins  
  
RUN mkdir -p /tmp/nagios-plugins && \  
wget \--no-check-certificate ${NAGIOS_PLUGINS_ARCHIVE} \  
-qO /tmp/nagios-plugins.tar.gz && \  
tar \--strip 1 -zxf /tmp/nagios-plugins.tar.gz -C /tmp/nagios-plugins && \  
cd /tmp/nagios-plugins && \  
./configure \  
\--prefix=${NAGIOS_HOME} \  
\--enable-perl-modules \  
\--enable-extra-opts \  
\--with-openssl=/usr/bin/openssl && \  
make && \  
make all && \  
make install && \  
make clean && \  
cd ~ && \  
rm -rf /tmp/nagios-plugins && \  
rm -rf /tmp/nagios-plugins.tar.gz  
  
# ---- nrpe  
  
RUN mkdir -p /tmp/nrpe && \  
wget \--no-check-certificate ${NAGIOS_NRPE_ARCHIVE} \  
-qO /tmp/nrpe.tar.gz && \  
tar \--strip 1 -zxf /tmp/nrpe.tar.gz -C /tmp/nrpe && \  
cd /tmp/nrpe && \  
./configure \  
\--prefix=${NAGIOS_HOME} \  
\--enable-ssl \  
\--with-opsys=linux \  
\--with-init-type=sysv \  
\--with-ssl=/usr/bin/openssl \  
\--with-ssl-lib=/usr/lib/x86_64-linux-gnu && \  
make && \  
make all && \  
make install && \  
make install-init && \  
make install-config && \  
make install-daemon && \  
make clean && \  
cd ~ && \  
rm -rf /tmp/nrpe && \  
rm -rf /tmp/nrpe.tar.gz  
  
# ---- nagios web  
  
RUN htpasswd -bc ${NAGIOS_HOME}/etc/htpasswd.users ${NAGIOS_WEB_USER}
${NAGIOS_WEB_PASS} && \  
chown ${NAGIOS_USER}:${NAGIOS_GROUP} ${NAGIOS_HOME}/etc/htpasswd.users  
  
RUN a2enconf nagios && \  
a2enmod cgi rewrite ssl  
  
# ---- supervisor  
  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/  
ADD service.conf /etc/supervisor/conf.d/  
  
# ---- workaround  
  
# FIXME: this is to resolve the following error message (Event Log)  
# * Error: Could not open log file '/opt/nagios/var/nagios.log' for reading!  
  
# FIXME: credentials in log file might exposed  
RUN touch /opt/nagios/var/nagios.log && chmod 0644 /opt/nagios/var/nagios.log  
  
# ---- misc  
  
EXPOSE 80 443 5666  
  
VOLUME [ "${NAGIOS_HOME}/var", "${NAGIOS_HOME}/etc" ]  
  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf" ]  


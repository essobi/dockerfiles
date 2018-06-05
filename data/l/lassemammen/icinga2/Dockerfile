# Dockerfile for icinga2 with icingaweb2  
# https://github.com/jjethwa/icinga2  
FROM debian:stretch  
  
MAINTAINER Jordan Jethwa  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV ICINGA2_FEATURE_GRAPHITE false  
ENV ICINGA2_FEATURE_GRAPHITE_HOST graphite  
ENV ICINGA2_FEATURE_GRAPHITE_PORT 2003  
ENV ICINGA_DIRECTOR_VERSION 1.4.3  
ENV ICINGA2_WEB_VERSION 2.5.1  
ENV NAGIOS_PLUGINS_RABBITMQ_VERSION 2.0.3  
RUN \  
apt-get -qq update && \  
apt-get -qqy upgrade && \  
apt-get install -yq wget gnupg apt-transport-https && \  
echo deb https://packages.sury.org/php/ stretch main | tee -a
/etc/apt/sources.list.d/php.list && \  
wget -qO - https://packages.sury.org/php/apt.gpg | apt-key add - && \  
apt-get update && \  
apt-get -qqy install --no-install-recommends bash sudo procps ca-certificates
supervisor mariadb-server mariadb-client apache2 pwgen unzip php7.1 php7.1-cli
php7.1-mysql php7.1-xml php7.1-common php7.1-ldap ssmtp mailutils vim
php7.1-curl python-mysqldb-dbg libnet-snmp-perl  
  
RUN \  
echo deb http://packages.icinga.com/debian icinga-stretch main | tee -a
/etc/apt/sources.list.d/icinga.list && \  
wget -qO - https://packages.icinga.org/icinga.key | apt-key add - && \  
apt-get -qq update && \  
apt-get -qqy install --no-install-recommends icinga2 icinga2-ido-mysql nagios-
plugins icingaweb2 icingacli curl libjson-perl liblwp-protocol-https-perl && \  
apt-get clean  
  
ADD content/ /  
ADD nagios/* /usr/lib/nagios/plugins/  
ADD rancher /usr/bin/rancher  
  
RUN chmod u+x /opt/supervisor/mysql_supervisor
/opt/supervisor/icinga2_supervisor /opt/supervisor/apache2_supervisor /opt/run
&& \  
chmod +s /bin/ping* /usr/bin/rancher  
  
# Temporary hack to get icingaweb2 modules via git  
RUN mkdir -p /etc/icingaweb2.dist/enabledModules && \  
wget --no-cookies
"https://github.com/Icinga/icingaweb2/archive/v${ICINGA2_WEB_VERSION}.zip" -O
/tmp/icingaweb2.zip && \  
unzip /tmp/icingaweb2.zip "icingaweb2-${ICINGA2_WEB_VERSION}/modules/doc/*"
"icingaweb2-${ICINGA2_WEB_VERSION}/modules/monitoring/*" -d "/tmp/icingaweb2"
&& \  
cp -R /tmp/icingaweb2/icingaweb2-${ICINGA2_WEB_VERSION}/modules/monitoring
/etc/icingaweb2.dist/modules/ && \  
cp -R /tmp/icingaweb2/icingaweb2-${ICINGA2_WEB_VERSION}/modules/doc
/etc/icingaweb2.dist/modules/ && \  
rm -rf /tmp/icingaweb2.zip /tmp/icingaweb2  
  
# Icinga Director  
RUN wget --no-cookies "https://github.com/Icinga/icingaweb2-module-
director/archive/v${ICINGA_DIRECTOR_VERSION}.zip" -O /tmp/director.zip && \  
unzip /tmp/director.zip -d "/tmp/director" && \  
cp -R /tmp/director/icingaweb2-module-director-${ICINGA_DIRECTOR_VERSION}/*
/etc/icingaweb2.dist/modules/director/ && \  
rm -rf /tmp/director.zip /tmp/director && \  
cp -R /etc/icingaweb2/* /etc/icingaweb2.dist/ && \  
cp -R /etc/icinga2 /etc/icinga2.dist && \  
rm -rf /etc/icingaweb2/modules  
  
RUN wget --no-cookies "https://github.com/nagios-plugins-rabbitmq/nagios-
plugins-rabbitmq/releases/download/${NAGIOS_PLUGINS_RABBITMQ_VERSION}/nagios-
plugins-rabbitmq-${NAGIOS_PLUGINS_RABBITMQ_VERSION}.libperl-monitoring-
plugin.zip" -O /tmp/nagios-plugins-rabbitmq.zip && \  
unzip /tmp/nagios-plugins-rabbitmq.zip -d "/tmp/nagios-plugins-rabbitmq" && \  
cp -R /tmp/nagios-plugins-rabbitmq/scripts /usr/lib/nagios/plugins-rabbitmq &&
\  
rm -rf /tmp/nagios-plugins-rabbitmq.zip /tmp/nagios-plugins-rabbitmq  
  
EXPOSE 80 443 5665  
# Initialize and run Supervisor  
ENTRYPOINT ["/opt/run"]  


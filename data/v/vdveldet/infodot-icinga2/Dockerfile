FROM centos:centos7  
  
MAINTAINER vdvelde.t@gmail.com  
  
# for systemd  
ENV container docker  
  
RUN yum -y update && \  
yum -y install epel-release && \  
yum -y install httpd hostname bind-utils cronie logrotate supervisor && \  
yum -y install passwd sed which pwgen psmisc mailx && \  
yum -y install mariadb-server mariadb-libs mariadb && \  
yum -y install unzip  
RUN yum -y install http://packages.icinga.org/epel/7/release/noarch/icinga-
rpm-release-7-1.el7.centos.noarch.rpm && \  
yum -y install nagios-plugins-all icinga2 icinga2-doc icinga2-ido-mysql
icingaweb2 icingacli php-ZendFramework php-ZendFramework-Db-Adapter-Pdo-Mysql  
  
  
# docs are not installed by default
https://github.com/docker/docker/issues/10650
https://registry.hub.docker.com/_/centos/  
# official docs are wrong, go for
http://superuser.com/questions/784451/centos-on-docker-how-to-install-doc-
files  
# we'll need that for mysql schema import for icingaweb2  
RUN [ -f /etc/rpm/macros.imgcreate ] && sed -i '/excludedocs/d'
/etc/rpm/macros.imgcreate || exit 0  
RUN [ -f /etc/yum.conf ] && sed -i '/nodocs/d' /etc/yum.conf || exit 0  
RUN yum -y reinstall icingaweb2  
  
RUN [ -f /etc/icinga2/features-available/graphite.conf ] && sed -i 's/\/\/host
= "127.0.0.1"/host = "graphite"/g' /etc/icinga2/features-
available/graphite.conf && \  
sed -i 's/\/\/port = 2003/port = 2003/g' /etc/icinga2/features-
available/graphite.conf  
  
  
# fixes at build time (we can't do that at user's runtime)  
# setuid problem https://github.com/docker/docker/issues/6828  
# 4755 ping is required for icinga user calling check_ping  
# can be circumvented for icinga2.cmd w/ mkfifo and chown  
# (icinga2 does not re-create the file)  
RUN mkdir -p /var/log/supervisor; \  
chmod 4755 /bin/ping /bin/ping6; \  
chown -R icinga:root /etc/icinga2; \  
mkdir -p /var/run/icinga2; \  
mkdir -p /var/log/icinga2; \  
chown icinga:icingacmd /var/run/icinga2; \  
chown icinga:icingacmd /var/log/icinga2; \  
mkdir -p /var/run/icinga2/cmd; \  
mkfifo /var/run/icinga2/cmd/icinga2.cmd; \  
chown -R icinga:icingacmd /var/run/icinga2/cmd; \  
chmod 2750 /var/run/icinga2/cmd; \  
chown -R icinga:icinga /var/lib/icinga2; \  
usermod -a -G icingacmd apache >> /dev/null; \  
mkdir -p /mnt/etc/icingaweb2; \  
cd /etc && rm -rf /etc/icingaweb2 && ln -sf /mnt/etc/icingaweb2; \  
chown root:icingaweb2 /mnt/etc/icingaweb2; \  
chmod 2770 /mnt/etc/icingaweb2; \  
mkdir -p /etc/icingaweb2/enabledModules; \  
chown -R apache:icingaweb2 /etc/icingaweb2/*; \  
mkdir -p /mnt/etc/icinga2; \  
cd /etc && rm -rf /etc/icinga2 && ln -sf /mnt/etc/icinga2; \  
chown icinga:icingaweb2 /mnt/etc/icinga2; \  
mkdir -p /mnt/var/lib/icinga2; \  
cd /var/lib/ && rm -rf /var/lib/icinga2 && ln -sf /mnt/var/lib/icinga2; \  
chown icinga:icingacmd /mnt/var/lib/icinga2/  
# configure PHP timezone  
RUN sed -i 's/;date.timezone =/date.timezone = UTC/g' /etc/php.ini  
  
# includes supervisor config  
ADD content/ /  
RUN chmod +x /usr/local/bin/*  
  
# ports (icinga2 api & cluster (5665), mysql (3306))  
EXPOSE 80 443 5665 3306  
  
# volumes  
VOLUME ["/var/lib/icinga2", "/usr/share/icingaweb2", "/var/lib/mysql", "/mnt"]  
  
  
ENTRYPOINT ["/usr/local/bin/icinga2_start"]  
  


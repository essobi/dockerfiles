FROM phusion/passenger-customizable:0.9.28  
MAINTAINER Rowan Wookey <admin@rwky.net>  
ENV HOME /root  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5862E31D && \  
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0F6DD8135234BF2B && \  
echo "deb http://ppa.launchpad.net/adiscon/v8-stable/ubuntu xenial main\ndeb-
src http://ppa.launchpad.net/adiscon/v8-stable/ubuntu xenial main" >
/etc/apt/sources.list.d/rsyslog.list && \  
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
&& \  
echo 'deb https://deb.nodesource.com/node_8.x xenial main' >
/etc/apt/sources.list.d/nodesource.list && \  
echo 'deb-src https://deb.nodesource.com/node_8.x xenial main' >>
/etc/apt/sources.list.d/nodesource.list && \  
apt-get update && \  
apt-get -y purge syslog-ng-core syslog-ng ntpdate isc-dhcp-common isc-dhcp-
client openssh-server openssh-sftp-server && \  
apt-get -yq -o Dpkg::Options::="--force-confold" upgrade && \  
apt-get -y -o Dpkg::Options::="--force-confold" install tzdata rsyslog nginx-
common nginx-extras passenger passenger-dev passenger-doc && \  
rm -rf /etc/my_init.d/00_regen_ssh_host_keys.sh && \  
rm -rf /etc/rsyslog.d/* && \  
rm -rf /etc/logrotate.d/* && \  
rm -f /etc/nginx/sites-enabled/* && \  
rm -rf /etc/service/sshd && \  
rm -rf /etc/service/syslog-ng && \  
rm -rf /etc/service/nginx-log-forwarder && \  
rm -rf /etc/service/syslog-forwarder && \  
rm -rf /var/log/* && \  
chown root:syslog /var/log && \  
mkdir -p /etc/service/exim && \  
mkdir -p /etc/service/rsyslog && \  
touch /etc/service/rsyslog/down && \  
touch /etc/service/exim/down && \  
touch /etc/service/nginx/down && \  
sed -i 's/# su root syslog/su root syslog/' /etc/logrotate.conf  
COPY image/rsyslog.conf /etc/rsyslog.conf  
COPY image/00-default.conf /etc/rsyslog.d/  
COPY image/rsyslog.logrotate /etc/logrotate.d/rsyslog  
COPY image/nginx/* /etc/nginx/conf.d/  
COPY image/nginx.conf /etc/nginx/nginx.conf  
COPY image/exim.run /etc/service/exim/run  
COPY image/rsyslog.run /etc/service/rsyslog/run  
COPY image/nginx.run /etc/service/nginx/run  
COPY image/pylogger /usr/local/bin/  
COPY image/cron.run /etc/service/cron/run  
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/* && \  
/usr/sbin/logrotate -v /etc/logrotate.conf  


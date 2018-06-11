FROM ubuntu:14.04  
MAINTAINER yeasy@github  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV DATA_DIR=/data \  
BIND_USER=bind \  
WEBMIN_VERSION=1.760  
RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
vim.tiny wget sudo net-tools ca-certificates unzip \  
bind9 perl libnet-ssleay-perl openssl \  
libauthen-pam-perl libpam-runtime libio-pty-perl \  
apt-show-versions python \  
&& wget
"http://prdownloads.sourceforge.net/webadmin/webmin_${WEBMIN_VERSION}_all.deb"
-P /tmp/ \  
&& dpkg -i /tmp/webmin_${WEBMIN_VERSION}_all.deb \  
&& rm -rf /tmp/webmin_${WEBMIN_VERSION}_all.deb \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /etc/cron.daily/apt /etc/cron.weekly/fstrim  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 53/udp 10000/tcp  
VOLUME ["${DATA_DIR}"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  


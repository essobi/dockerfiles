FROM phusion/baseimage:0.9.18  
MAINTAINER Kyle McNally <kamcnally@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV IREDMAIL_VERSION 0.9.5-1  
# Install some necessary packages  
RUN export TERM=xterm \  
&& apt-get -q update \  
&& apt-get install -y -q --no-install-recommends \  
wget \  
bzip2 \  
dovecot-core \  
dovecot-lmtpd \  
dovecot-sieve \  
dovecot-managesieved \  
dovecot-imapd \  
dovecot-mysql \  
dovecot-pop3d \  
openssl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt/iredmail  
  
#Copy iRedMail install and configuration file  
COPY ./install.sh /etc/my_init.d/00_install_iredmail.sh  
COPY ./config /opt/config/  
  
#Copy in service/daemon start scripts  
COPY ./my_init.d/ /etc/my_init.d/  
  
#Copy in certiface update script  
COPY ./certs/ /opt/certs/  
  
RUN chmod +x /etc/my_init.d/*.sh \  
&& chmod +x /opt/certs/update_certs.sh  
  
# Open Ports:  
# Nginx: 443/tcp  
# Postfix: 587/tcp  
# Dovecot: 993/tcp, 995/tcp  
EXPOSE 443 587 993 995  
VOLUME ["/var/vmail/","/opt/certs/","/opt/config/"]  
  
# Start all services  
CMD ["/sbin/my_init"]


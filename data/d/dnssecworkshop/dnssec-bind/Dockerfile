# Image: dnssec-bind  
# Startup a docker container with sshd and BIND 9.10  
FROM ubuntu:latest  
  
MAINTAINER dape16 "dockerhub@arminpech.de"  
LABEL RELEASE=20171013-2152  
  
# Install software  
RUN apt-get update  
RUN apt-get purge -y exim4 rpcbind portmap at avahi-daemon  
RUN apt-get upgrade -y  
RUN apt-get install -y --no-install-recommends \  
tcpdump traceroute curl wget git less screen \  
vim nano ntp ntpdate telnet syslog-ng zip unzip \  
man rsync ca-certificates lsof sudo  
RUN apt-get install -y --no-install-recommends \  
openssh-server supervisor cron  
RUN apt-get install -y --no-install-recommends \  
bind9 dnsutils libnet-dns-sec-perl whois \  
openssl ldnsutils  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get clean  
  
# Set login data  
RUN echo 'root:root' | chpasswd  
  
# Configure sshd  
RUN rm /etc/ssh/ssh_host_*  
RUN ssh-keygen -A  
RUN chmod 600 /etc/ssh/ssh_host_*  
RUN sed -i "s/PermitRootLogin.*/PermitRootLogin yes/" /etc/ssh/sshd_config  
RUN echo "UseDNS no" >> /etc/ssh/sshd_config  
RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional
pam_loginuid.so/' \  
/etc/pam.d/sshd  
  
RUN mkdir -p /var/run/sshd  
  
# Prepare bind  
RUN rm -rf /etc/bind  
RUN mkdir -p /etc/bind/zones /etc/bind/keys /etc/bind/scripts  
RUN mkdir -p /var/log/named /var/run/named /var/lib/bind /var/cache/bind  
RUN chown -R root:bind /var/log/named /var/run/named \  
/var/lib/bind /var/cache/bind /etc/bind/zones  
RUN chmod 775 /var/log/named /var/run/named/ \  
/var/lib/bind /var/cache/bind /etc/bind/zones  
  
RUN rndc-confgen | awk '/^key "rndc-key"/,/^};/ {print}' > /etc/bind/rndc.key  
  
# vim: set syntax=docker tabstop=2 expandtab:  


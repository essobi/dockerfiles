FROM debian:8  
  
MAINTAINER Ivan Udovin <wilcot@ya.ru>  
  
RUN \  
export TERM=linux \  
&& apt-get -y update \  
&& apt-get -y install \  
curl \  
&& curl -O http://vestacp.com/pub/vst-install-debian.sh \  
&& bash vst-install-debian.sh \  
\--interactive no \  
\--password admin \  
\--nginx yes \  
\--phpfpm yes \  
\--apache no \  
\--named yes \  
\--remi no \  
\--vsftpd no \  
\--proftpd no \  
\--iptables no \  
\--fail2ban no \  
\--quota no \  
\--exim yes \  
\--dovecot yes \  
\--spamassassin no \  
\--clamav no \  
\--mysql yes \  
\--postgresql no \  
&& rm -f vst-install-debian.sh \  
&& apt-get -y clean  
  
ENV VESTA=/usr/local/vesta  
  
RUN \  
cd /etc/init.d \  
  
&& ./ssh stop \  
&& update-rc.d -f ssh disable \  
  
&& ./nginx stop \  
&& update-rc.d -f nginx disable \  
  
&& ./bind9 stop \  
&& update-rc.d -f bind9 disable \  
  
&& ./php5-fpm stop \  
&& update-rc.d -f php5-fpm disable \  
  
&& ./mysql stop \  
&& update-rc.d -f mysql disable \  
  
&& ./exim4 stop \  
&& update-rc.d -f exim4 disable \  
  
&& ./dovecot stop \  
&& update-rc.d -f dovecot disable \  
  
&& ./cron stop \  
&& update-rc.d -f cron disable \  
  
&& ./vesta stop \  
&& update-rc.d -f vesta disable \  
  
&& cd /usr/local/vesta/bin \  
  
&& ./v-delete-web-domains admin \  
&& ./v-delete-dns-domains admin \  
&& ./v-delete-mail-domains admin \  
  
&& cd /usr/local/vesta/data/ips \  
  
&& mv -f 172.*.*.* 127.0.0.1 \  
&& sed -i s/NAT=\'[0-9.]*\'/NAT=\'0.0.0.0\'/g 127.0.0.1 \  
  
&& cd /usr/local/vesta/data/users/admin \  
  
&& sed -i s/\'admin@[0-9a-f]*.example.com\'/\'admin@localhost.ltd\'/g
user.conf \  
  
&& cd /usr/local/vesta/bin \  
  
&& ./v-add-web-domain admin localhost.ltd \  
  
&& mkdir /.copy \  
  
&& mv -f /home /.copy/home \  
&& rm -rf /home \  
  
&& mkdir /.copy/vesta \  
  
&& mkdir /.copy/vesta/usr \  
&& mkdir /.copy/vesta/usr/local \  
  
&& mv -f /usr/local/vesta /.copy/vesta/usr/local/vesta \  
&& rm -rf /usr/local/vesta \  
&& ln -s /vesta/usr/local/vesta /usr/local/vesta \  
  
&& mkdir /.copy/vesta/etc \  
  
&& mv -f /etc/passwd /.copy/vesta/etc/passwd \  
&& rm -f /etc/passwd \  
  
&& mv -f /etc/group /.copy/vesta/etc/group \  
&& rm -f /etc/group \  
  
&& mv -f /etc/shadow /.copy/vesta/etc/shadow \  
&& rm -f /etc/shadow \  
  
&& mv -f /etc/gshadow /.copy/vesta/etc/gshadow \  
&& rm -f /etc/gshadow \  
  
&& mv -f /etc/nginx /.copy/vesta/etc/nginx \  
&& rm -rf /etc/nginx \  
&& ln -s /vesta/etc/nginx /etc/nginx \  
  
&& mkdir /.copy/vesta/var \  
&& mkdir /.copy/vesta/var/lib \  
  
&& mv -f /var/lib/mysql /.copy/vesta/var/lib/mysql \  
&& rm -rf /var/lib/mysql \  
&& ln -s /vesta/var/lib/mysql /var/lib/mysql  
  
COPY vesta.sh /vesta.sh  
  
RUN chmod 0744 /vesta.sh  
  
ENTRYPOINT ["/vesta.sh"]  
  
VOLUME ["/home", "/vesta"]  
  
EXPOSE 80 443 8083 22 53 3306  


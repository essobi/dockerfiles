FROM ubuntu:14.04  
MAINTAINER Kon Hondros konhondros@icloud.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y wget curl postfix-mysql dovecot-mysql dovecot-imapd
dovecot-lmtpd php5 php5-fpm php5-common php5-mysql spamassassin php5-imap
postfixadmin roundcube  
RUN adduser vmail -q --home /var/vmail --uid 1150 --disabled-password --gecos
""  
RUN mkdir -p /data/mydata  
  
# Install Postfix  
RUN wget -q
http://downloads.sourceforge.net/project/postfixadmin/postfixadmin/postfixadmin-2.93/postfixadmin-2.93.tar.gz  
RUN tar -C /var/www/html/ -xf postfixadmin-2.93.tar.gz  
RUN ln -s /var/www/html/postfixadmin-2.93/ /var/www/html/postfixadmin  
RUN rm postfixadmin-2.93.tar.gz  
  
# Install Roundcube  
RUN wget -q
http://downloads.sourceforge.net/project/roundcubemail/roundcubemail/1.1.4/roundcubemail-1.1.4-complete.tar.gz  
RUN tar -C /var/www/html/ -xf roundcubemail-1.1.4-complete.tar.gz  
RUN ln -s /var/www/html/roundcubemail-1.1.4 /var/www/html/roundcubemail  
RUN chown :syslog /var/log/  
RUN chmod 775 /var/log/  
RUN rm roundcubemail-1.1.4-complete.tar.gz  
  
# Install Caddy  
RUN wget -q
https://github.com/mholt/caddy/releases/download/v0.9.5/caddy_linux_amd64.tar.gz  
RUN mkdir /caddy  
RUN tar -C /caddy -xf caddy_linux_amd64.tar.gz && rm caddy_linux_amd64.tar.gz  
RUN cp /caddy/caddy_linux_amd64 /usr/local/bin/caddy  
RUN rm -rf /caddy  
  
# to generate your dhparam.pem file  
RUN mkdir -p /etc/ssl/private  
RUN openssl dhparam -out /etc/ssl/private/dhparams.pem 2048  
  
# Install acme.sh  
RUN curl https://get.acme.sh | sh  
  
COPY roundcube_postfixadmin.sql /root/  
  
RUN sed -i "s/ENABLED=0/ENABLED=1/g" /etc/default/spamassassin  
  
COPY entrypoint.sh /root/entrypoint.sh  
  
COPY dovecot /etc/dovecot  
COPY postfix /etc/postfix  
  
COPY postfixadmin /var/www/html/postfixadmin  
COPY roundcubemail/config /var/www/html/roundcubemail/config  
  
VOLUME [ "/var/log/", "/var/vmail/", "/var/lib/mysql", "/ssl", "/root/.caddy"
]  
  
EXPOSE 25 80 143 443 465 993  
ENTRYPOINT /root/entrypoint.sh  


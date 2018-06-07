#  
FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y wget postfix-mysql dovecot-mysql dovecot-imapd dovecot-
pop3d dovecot-lmtpd spamassassin php5-imap postfixadmin roundcube  
RUN adduser vmail -q --home /var/vmail --uid 1150 --disabled-password --gecos
""  
  
RUN wget -q
http://downloads.sourceforge.net/project/postfixadmin/postfixadmin/postfixadmin-2.93/postfixadmin-2.93.tar.gz  
RUN tar -C /var/www/html/ -xf postfixadmin-2.93.tar.gz  
RUN ln -s /var/www/html/postfixadmin-2.93/ /var/www/html/postfixadmin  
  
RUN wget -q
http://downloads.sourceforge.net/project/roundcubemail/roundcubemail/1.1.4/roundcubemail-1.1.4-complete.tar.gz  
RUN tar -C /var/www/html/ -xf roundcubemail-1.1.4-complete.tar.gz  
RUN ln -s /var/www/html/roundcubemail-1.1.4 /var/www/html/roundcubemail  
RUN chown :syslog /var/log/  
RUN chmod 775 /var/log/  
  
COPY roundcube_postfixadmin.sql /  
  
RUN sed -i "s/ENABLED=0/ENABLED=1/g" /etc/default/spamassassin  
  
COPY run.sh /run.sh  
COPY dovecot /etc/dovecot  
COPY postfix /etc/postfix  
COPY postfixadmin /var/www/html/postfixadmin  
COPY roundcubemail/config /var/www/html/roundcubemail/config  
  
VOLUME [ "/var/log/", "/var/vmail/", "/var/lib/mysql" ]  
  
EXPOSE 25 80 110 143 465 993 995  
ENTRYPOINT /run.sh  


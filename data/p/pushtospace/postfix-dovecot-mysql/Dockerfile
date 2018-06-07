FROM pushtospace/ubuntu  
  
MAINTAINER Gino Jongenelen <g.jongenelen@pushto.space>  
  
RUN apt-get install tzdata postfix-pcre -y  
RUN cp /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime  
  
#############################  
### Install Postfix & Dovecot  
#############################  
RUN apt-get install -y syslog-ng-core syslog-ng postfix postfix-mysql dovecot-
core dovecot-sieve dovecot-imapd dovecot-lmtpd dovecot-mysql redis-tools  
  
ADD postfix/* /etc/postfix/  
ADD dovecot/* /etc/dovecot/  
ADD ./start.sh /root  
  
RUN groupadd -g 5000 vmail && useradd -g vmail -u 5000 vmail -d /home/vmail &&
mkdir /home/vmail && chown -R vmail:vmail /home/vmail && chmod +x
/root/start.sh  
  
#############################  
### Install Spam assassin  
#############################  
RUN apt-get install spamassassin spamc libdbi-perl libdbd-mysql-perl -y  
RUN groupadd spamd && useradd -g spamd -s /bin/false -d /var/log/spamassassin
spamd && mkdir /var/log/spamassassin && chown spamd:spamd
/var/log/spamassassin  
COPY spamassassin/default /etc/default/spamassassin  
COPY spamassassin/local.cf /etc/spamassassin/local.cf  
  
#############################  
### Install Spf-policy  
#############################  
RUN apt-get install postfix-policyd-spf-python -y  
  
  
CMD ["/root/start.sh"]


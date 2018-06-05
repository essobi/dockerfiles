FROM ubuntu  
  
MAINTAINER Bram <bram-dockerfiles-postfix-dovecot@grmbl.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-divert --local \--rename --add /sbin/initctl && ln -sf /bin/true
/sbin/initctl  
RUN apt-get update && apt-get -y install openssh-server rsyslog sqlite3 mysql-
client \  
postfix postfix-cluebringer-sqlite3 postfix-mysql postfix-pcre \  
dovecot-core dovecot-antispam dovecot-mysql dovecot-sqlite dovecot-imapd
dovecot-pop3d dovecot-sieve dovecot-managesieved \  
amavisd-new spamassassin spamc pyzor razor gawk  
  
RUN apt-get install -y clamav clamav-base clamav-daemon clamav-freshclam
clamassassin postgrey  
RUN touch /etc/ssh/recreate-ssh-keys-bang-bang  
  
EXPOSE 22 25 110 143 587  
VOLUME /etc /var/spool /var/log  
  
ADD run.sh /run.sh  
  
CMD /run.sh  


FROM debian:jessie  
MAINTAINER dennis@moellegaard.dk  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get -qy --no-install-recommends install supervisor postfix rsyslog \  
dovecot-core dovecot-lmtpd dovecot-imapd dovecot-pop3d dovecot-sieve dovecot-
managesieved \  
opendkim postfix-policyd-spf-perl opendmarc \  
amavisd-new spamassassin clamav clamav-daemon zoo unzip bzip2 libnet-ph-perl
libnet-snpp-perl libnet-telnet-perl nomarch lzop \  
postgrey && \  
rm -rf /var/lib/apt/lists/*  
  
COPY assets/ /  
  
VOLUME /var/mail  
VOLUME /var/lib/clamav  
VOLUME /var/lib/postgrey  
VOLUME /config  
  
# smtp, pop3, imap2, ssmtp/smtps, submission, pop3s, manage sieve  
EXPOSE 25 110 143 465 587 993 995 4190  
CMD ["/root/run.sh"]  


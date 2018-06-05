FROM debian:jessie  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -q update  
RUN apt-get -qy upgrade  
RUN apt-get -qy remove exim4  
RUN apt-get -qy install postfix postfix-pgsql openssl rsyslog \  
telnet opendkim opendkim-tools  
RUN apt-get autoclean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /etc/ssl/private/  
RUN chmod 710 /etc/ssl/private  
RUN openssl dhparam -out /etc/ssl/private/dhparams.pem 1024  
  
# Log files must exist, or nothing gets written to them  
RUN touch /var/log/mail.log  
RUN touch /var/log/mail.err  
RUN touch /var/log/mail.info  
RUN touch /var/log/mail.warn  
  
# Needed for postfix to function  
RUN ln -snf /etc/ssl /var/spool/postfix/etc/ssl  
  
# You should mount /etc/opendkim/keys as a volume to retain  
# your dkim key across restarts.  
RUN mkdir -p /etc/opendkim  
RUN mkdir -p /etc/opendkim/keys  
VOLUME /etc/opendkim/keys  
COPY SigningTable /etc/opendkim/SigningTable  
COPY TrustedHosts /etc/opendkim/TrustedHosts  
# Copy opendkim config files  
COPY opendkim.conf /etc/opendkim.conf  
COPY default-opendkim /etc/default/opendkim  
  
# Copy config files for postfix  
COPY main.cf /etc/postfix/main.cf  
COPY master.cf /etc/postfix/master.cf  
COPY pgsql-domains.cf /etc/postfix/pgsql-domains.cf  
COPY pgsql-aliases.cf /etc/postfix/pgsql-aliases.cf  
COPY pgsql-mailboxes.cf /etc/postfix/pgsql-mailboxes.cf  
  
COPY run.sh /usr/local/bin/run.sh  
  
CMD /usr/local/bin/run.sh  


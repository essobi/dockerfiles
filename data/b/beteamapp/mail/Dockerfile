FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV maildomain mail.example.org  
ENV domain example.org  
  
RUN echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-
set-selections  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
dovecot-core \  
dovecot-imapd \  
dovecot-managesieved \  
# dovecot-mysql \  
# dovecot-pop3d \  
postfix \  
# postfix-mysql \  
rsyslog \  
&& rm -rf /var/lib/apt/lists/*  
  
  
RUN groupadd -g 5000 vmail \  
&& useradd -g vmail -u 5000 vmail -d /var/mail/vmail -m  
  
COPY ./aliases /etc/aliases  
RUN newaliases  
  
# Postfix Configuration  
COPY ./postfix/main.cf /etc/postfix/main.cf  
COPY ./postfix/master.cf /etc/postfix/master.cf  
  
# Dovecot Configuration  
COPY ./dovecot/conf.d/01-mail-stack-delivery.conf /etc/dovecot/conf.d/01-mail-
stack-delivery.conf  
COPY ./dovecot/conf.d/10-auth.conf /etc/dovecot/conf.d/10-auth.conf  
COPY ./dovecot/conf.d/10-mail.conf /etc/dovecot/conf.d/10-mail.conf  
COPY ./dovecot/conf.d/10-ssl.conf /etc/dovecot/conf.d/10-ssl.conf  
COPY ./dovecot/conf.d/15-mailboxes.conf /etc/dovecot/conf.d/15-mailboxes.conf  
  
# Sieve Configuration  
RUN mkdir /var/mail/vmail/sieve-before \  
&& mkdir /var/mail/vmail/sieve-after  
  
COPY ./sieve/base.sieve /var/mail/vmail/sieve-before/base.sieve  
  
RUN sievec /var/mail/vmail/sieve-before/base.sieve \  
&& chown -R vmail:vmail /var/mail/vmail/sieve-before \  
&& chown -R vmail:vmail /var/mail/vmail/sieve-after  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
VOLUME ["/var/mail/vmail"]  
EXPOSE 25 143 465 587 993  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["tail"]  


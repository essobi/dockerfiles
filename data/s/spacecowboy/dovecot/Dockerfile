FROM debian:jessie  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -q update  
RUN apt-get -qy upgrade  
RUN apt-get -qy remove exim4  
RUN apt-get -qy install dovecot-lmtpd dovecot-pgsql \  
dovecot-managesieved dovecot-sieve \  
dovecot-imapd dovecot-pop3d telnet \  
postgresql-client  
RUN apt-get autoclean && rm -rf /var/lib/apt/lists/*  
  
# Dovecot needs to run as its own user, here called 'vmail'  
RUN adduser --system --no-create-home --uid 500 --group --disabled-password \  
\--disabled-login --gecos 'dovecot virtual mail user' vmail  
  
# Mail is stored under /var/vmail/domain/user/mail  
# with user specific stuff in /var/vmail/domain/user  
COPY dovecot.conf /etc/dovecot/dovecot.conf  
COPY dovecot-sql.conf /etc/dovecot/dovecot-sql.conf  
RUN mkdir -p /etc/dovecot/sieve-filters  
COPY gpgit /etc/dovecot/sieve-filters/gpgit  
RUN mkdir -p /etc/dovecot/scripts  
COPY globalsieve /etc/dovecot/scripts/default.sieve  
  
# make mail dirs  
RUN mkdir -p /var/vmail  
  
VOLUME /var/vmail  
  
COPY run.sh /usr/local/bin/run.sh  
  
CMD /usr/local/bin/run.sh  


FROM jbonachera/arch  
MAINTAINER Julien BONACHERA <julien@bonachera.fr>  
ENTRYPOINT /sbin/entrypoint.sh  
EXPOSE 24 143 993 4190  
VOLUME ["/srv/vmail", "/etc/dovecot/auth"]  
HEALTHCHECK \--interval=10s --timeout=3s CMD doveadm service status || exit 1  
RUN pacman -S --noconfirm dovecot pigeonhole  
RUN groupadd -g 5000 vmail  
RUN useradd -r vmail -u 5000 -g 5000  
COPY dovecot.conf /etc/dovecot/dovecot.conf  
COPY conf.d/* /etc/dovecot/conf.d/  
COPY templates /etc/dovecot/templates/  
COPY scripts/* /usr/local/bin/  
ADD entrypoint.sh /sbin/entrypoint.sh  
  


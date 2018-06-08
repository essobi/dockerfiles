FROM alpine  
  
MAINTAINER MarvAmBass (https://github.com/ServerContainers)  
  
RUN apk update \  
&& apk add runit \  
rsyslog \  
openssl \  
mariadb-client \  
\  
&& echo ">> configure logging" \  
&& cat /etc/rsyslog.conf | grep -v '^#' | grep '^\$' | sed '/imklog.so/d' >
/etc/rsyslog.conf.new \  
&& mv /etc/rsyslog.conf.new /etc/rsyslog.conf \  
&& echo '*.* /dev/stdout' >> /etc/rsyslog.conf \  
\  
&& echo ">> install mail server packages" \  
&& apk add dovecot \  
dovecot-mysql \  
dovecot-pigeonhole-plugin \  
&& apk add postfix \  
postfix-mysql \  
&& rm -rf /var/cache/apk/* \  
\  
\  
&& echo ">> add user" \  
&& deluser vmail \  
&& adduser -g vmail -u 5000 vmail -h /var/vmail -s /bin/false -D \  
\  
&& touch /etc/mtab \  
\  
&& openssl dhparam -out /etc/postfix/dh1024.pem 1024 \  
&& openssl dhparam -out /etc/postfix/dh512.pem 512  
  
COPY config /etc/  
  
# postfix  
EXPOSE 25 465 587  
# dovecot  
EXPOSE 110 143 993 995 4190  
VOLUME ["/etc/postfix/tls", "/etc/postfix/additional", "/var/vmail"]  
  
COPY scripts /usr/local/bin  
COPY mysql-data-scheme.sql /mysql-data-scheme.sql  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  


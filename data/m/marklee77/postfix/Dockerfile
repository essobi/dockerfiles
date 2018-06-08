FROM marklee77/supervisor:alpine  
LABEL maintainer="Mark Stillwell <mark@stillwell.me>"  
  
RUN apk update && \  
apk del ssmtp && \  
apk add ca-certificates postfix && \  
rm -rf /etc/postfix/* && \  
apk add postfix-ldap && \  
rm -rf /var/cache/apk/* && \  
mkdir -m 0755 /etc/postfix/conf.d /etc/ssl/postfix  
  
COPY root/etc/my_init.d/10-postfix-setup /etc/my_init.d/  
RUN chmod 0755 /etc/my_init.d/10-postfix-setup  
  
COPY root/etc/supervisor/conf.d/postfix.conf /etc/supervisor/conf.d/  
RUN chmod 0644 /etc/supervisor/conf.d/postfix.conf  
  
EXPOSE 25 587  


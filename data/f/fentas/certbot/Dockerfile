FROM alpine:3.6  
ENV CERTBOT_DOMAINS="/certbot.domains"  
ENV LE_STAGING=1  
ENV LE_EMAIL="replace.me@example.com"  
ENV LE_RSA_KEY_SIZE=2048  
ENV LE_CRON_TIME="@daily"  
RUN apk add --no-cache \  
bash ca-certificates zip grep curl certbot sed openssl coreutils util-linux  
  
VOLUME /var/acme-webroot  
VOLUME /etc/letsencrypt  
VOLUME /var/log/  
  
COPY data/ /  
ENTRYPOINT [ "/entrypoint.sh" ]  


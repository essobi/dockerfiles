FROM alpine:3.6  
ENV UID=0 GID=0 \  
STAGING=true \  
CRON_PERIOD=7d  
  
# Create user  
RUN addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx  
  
# Install nginx and other dependencies  
RUN apk -U upgrade && apk add \  
bash \  
libssl1.0 \  
openssl \  
certbot \  
nginx \  
s6 \  
ca-certificates \  
su-exec \  
tzdata  
  
# Create letsencrypt directories  
RUN mkdir -p /etc/letsencrypt \  
&& mkdir -p /etc/letsencrypt/archive \  
&& mkdir -p /etc/letsencrypt/live/self-signed \  
&& mkdir -p /data/letsencrypt \  
&& rm -rf /var/cache/apk/* /tmp/* /root/.gnupg  
  
# Copy files to destination  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY run.sh /usr/local/bin/run.sh  
COPY s6.d /etc/s6.d  
COPY generate-certs /usr/local/bin/generate-certs  
COPY letsencrypt-setup /usr/local/bin/letsencrypt-setup  
COPY letsencrypt-renew /usr/local/bin/letsencrypt-renew  
  
# Make scripts executable  
RUN chmod +x /usr/local/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
EXPOSE 80 443  
CMD ["run.sh"]  


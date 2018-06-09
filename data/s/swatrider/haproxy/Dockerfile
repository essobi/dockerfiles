FROM dockercloud/haproxy:1.6.2  
RUN apk add --update \  
bash \  
inotify-tools \  
openssl \  
&& rm -rf /var/cache/apk/*  
  
RUN ln -sf /dev/stdout /var/log/haproxy.log  
  
ENV LIVE_CERT_FOLDER="/etc/letsencrypt/live"  
ENV PATH="/opt/haproxy/bin:$PATH"  
COPY . /opt/haproxy  
  
CMD ["entrypoint.sh", "dockercloud-haproxy"]  


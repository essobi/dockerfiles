FROM krumware/dockercloud-haproxy-new:latest  
  
RUN apk add --update \  
bash \  
inotify-tools \  
openssl \  
&& rm -rf /var/cache/apk/*  
  
ENV LIVE_CERT_FOLDER="/etc/letsencrypt/live"  
ENV PATH="/opt/haproxy/bin:$PATH"  
COPY . /opt/haproxy  
RUN chmod +x /opt/haproxy/bin/*.sh  
  
CMD ["entrypoint.sh", "dockercloud-haproxy"]  


FROM dockercloud/haproxy:1.5.3  
RUN apk add --update \  
bash \  
inotify-tools \  
&& rm -rf /var/cache/apk/*  
  
ENV CERT_FOLDER="/certs"  
ENV LIVE_CERT_FOLDER="/etc/letsencrypt/live"  
ENV PATH="/opt/haproxy/bin:$PATH"  
COPY . /opt/haproxy/  
  
CMD ["entrypoint.sh", "dockercloud-haproxy"]  


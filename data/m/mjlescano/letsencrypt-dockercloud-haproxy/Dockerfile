FROM certbot/certbot:v0.12.0  
RUN apk add --update \  
bash \  
tini \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /etc/letsencrypt  
  
ENV VIRTUAL_HOST="*/.well-known/acme-challenge/*"  
ENV VIRTUAL_HOST_WEIGHT="999"  
ENV PATH="/opt/letsencrypt/bin:$PATH"  
COPY . /opt/letsencrypt/  
RUN ln -fs /opt/letsencrypt/bin/update-certs.sh /etc/periodic/daily/  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["entrypoint.sh", "crond", "-f"]  


FROM alpine:3.4  
RUN apk add --update \  
bash \  
certbot \  
tini \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 80  
VOLUME /etc/letsencrypt  
  
ENV VIRTUAL_HOST="*/.well-known/acme-challenge/*"  
ENV VIRTUAL_HOST_WEIGHT="999"  
ENV PATH="/opt/letsencrypt/bin:$PATH"  
COPY . /opt/letsencrypt/  
  
RUN chmod +x /opt/letsencrypt/bin/*.sh  
RUN chmod +x /opt/letsencrypt/bin/entrypoint.sh  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["entrypoint.sh", "crond", "-f"]  


FROM alpine:3.5  
RUN apk add --update \  
bash \  
certbot \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 80  
VOLUME /etc/letsencrypt  
  
ENV VIRTUAL_HOST="*/.well-known/acme-challenge/*"  
ENV VIRTUAL_HOST_WEIGHT="999"  
COPY update-certs /usr/local/bin/  
  
CMD ["update-certs"]  


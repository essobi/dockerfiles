FROM traefik:1.3.6-alpine  
  
ENV TRAEFIK_USER admin \  
TRAEFIK_USER_PASSWORD Tigrou007 \  
IGLU_DOMAIN iglu.com  
  
ADD traefikinit.sh /traefikinit.sh  
RUN chmod +x /traefikinit.sh  
ADD traefik.toml /etc/traefik/traefik.toml  
  
RUN apk update && \  
apk add apache2-utils openssl  
  
ENTRYPOINT ["/traefikinit.sh"]  
  
CMD ["traefik"]  


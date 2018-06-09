FROM alpine:3.5  
RUN apk add --no-cache certbot && mkdir /home/acme && mkdir /etc/letsencrypt
&& mkdir /etc/letsencrypt/c  
  
VOLUME /home/toyorg/letsencrypt:/etc/letsencrypt  
VOLUME /var/lib/letsencrypt  
VOLUME /home/toyorg/traefik/certs/acme:/home/acme  
  
COPY cert.sh cert.sh  
COPY copy.sh copy.sh  
COPY check.sh check.sh  
RUN chmod +x cert.sh && chmod +x copy.sh && chmod +x check.sh && echo "0 0 * *
* /bin/sh -c check.sh" >> /etc/crontabs/root  
  
EXPOSE 80 443  
CMD ./cert.sh  


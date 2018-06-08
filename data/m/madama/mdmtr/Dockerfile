FROM goldy/tor-hidden-service  
  
RUN apk add --update nginx curl  
RUN chown -R nginx:www-data /var/lib/nginx  
RUN mkdir -p /run/nginx  
RUN mkdir -p /var/tmp/nginx  
RUN rm /etc/nginx/conf.d/default.conf  
  
RUN apk add --update varnish  
  
RUN rm -rf /var/cache/apk/*  
  
COPY nginx /etc/nginx  
COPY varnish /etc/varnish  
  
ADD entrypoint-config.yml /  
  
RUN sed -i "s/SocksPort 0/SOCKSPort 0.0.0.0:9050/" /var/local/tor/torrc.tpl  
HEALTHCHECK CMD curl --socks5 localhost:9050 --socks5-hostname localhost:9050
-f http://32pbf32xi6ccm63z.onion/ || exit 1  
  
EXPOSE 8888 8080  
RUN chmod 777 -R /var/tmp  
RUN chmod 777 -R /var/log  
RUN chmod 777 -R /var/lib/nginx  
RUN chmod 777 -R /run/nginx  
RUN chmod 777 -R /etc/varnish  
RUN chmod 777 -R /var/lib/varnish  
RUN chmod 777 -R /var/local/tor  
RUN chmod 777 -R /var/lib/tor  
RUN chmod 777 -R /var/lib/tor/hidden_service  
RUN mkdir -p /usr/var/local/tor  
RUN mkdir -p /usr/local/var/tor  
RUN chmod 777 -R /usr/var/local/tor  
RUN chmod 777 -R /usr/local/var/tor  
  
#RUN adduser -D myuser  
#USER myuser  
#RUN printf "\nUser $(whoami)" >> /var/local/tor/torrc.tpl  


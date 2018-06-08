FROM nginx:mainline-alpine  
  
RUN apk add --no-cache wget ca-certificates supervisor coreutils curl  
  
RUN wget -q
https://github.com/kelseyhightower/confd/releases/download/v0.12.0/confd-0.12.0-linux-
amd64 -O /usr/bin/confd \  
&& echo "df491dcef39fd2798dd34485aa8de0408c65f8e0 /usr/bin/confd" | sha1sum -c
- \  
&& chmod +x /usr/bin/confd \  
&& mkdir -p /etc/confd/conf.d \  
&& mkdir -p /etc/confd/templates  
  
RUN mkdir -p /var/cache/nginx/instances_static/ \  
&& chown 33:33 /var/cache/nginx/instances_static/  
  
RUN mkdir -p /var/www/instances_common/  
  
COPY confd /etc/confd  
COPY app /app/  
COPY nginx_common.conf /etc/nginx/conf.d/default.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/letsencrypt"]  
VOLUME ["/var/cache/nginx/instances_static/"]  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["supervisord", "-c", "/app/supervisord.conf"]  
  
HEALTHCHECK \--interval=30s --timeout=5s \  
CMD curl -f http://localhost/ || exit 1  


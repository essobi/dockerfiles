FROM nginx:1.10.1-alpine  
  
# timezone  
RUN apk add --no-cache tzdata && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
apk del tzdata  
  
COPY nginx.conf.template /etc/nginx/nginx.conf.template  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENV CLIENT_MAX_BODY=10m \  
UPSTREAM=http://upstream_host:8000  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD /usr/sbin/nginx -c /etc/nginx/nginx.conf


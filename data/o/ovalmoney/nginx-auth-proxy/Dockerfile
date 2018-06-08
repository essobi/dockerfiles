FROM nginx:stable-alpine  
  
# for htpasswd command  
RUN apk --no-cache add \  
apache2-utils  
RUN rm -f /etc/nginx/conf.d/*  
  
ENV SERVER_NAME example.com  
ENV PORT 80  
ENV CLIENT_MAX_BODY_SIZE 1m  
ENV PROXY_READ_TIMEOUT 60s  
ENV WORKER_PROCESSES auto  
  
COPY files/run.sh /  
COPY files/nginx.conf.tmpl /  
  
ENTRYPOINT ["/run.sh"]  


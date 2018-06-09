FROM nginx:mainline-alpine  
  
RUN apk add --update --no-cache \  
dumb-init \  
gettext \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
COPY nginx-redirect.conf /etc/nginx/nginx-redirect.conf  
  
WORKDIR /opt/simple-redirect  
COPY start.sh ./start.sh  
  
CMD ["/opt/simple-redirect/start.sh"]  


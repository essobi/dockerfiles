FROM nginx:alpine  
  
ENV TINI_VERSION v0.10.0  
RUN apk add --no-cache --update tini  
RUN apk add --no-cache unzip curl && \  
curl -sL -o /tmp/docker-nginx.zip https://github.com/oondeo/docker-
nginx/archive/master.zip && \  
cd /tmp && unzip /tmp/docker-nginx.zip && \  
mv /tmp/docker-nginx-master/common/wordpress/global
/etc/ngnix/wordpress_params && \  
rm -rf /tmp/docker-nginx-master/common/wordpress && \  
mv /tmp/docker-nginx-master/common/* /etc/nginx && \  
apk del unzip curl && rm -rf /tmp/*  
  
RUN chmod +x /sbin/tini  
ENTRYPOINT ["/sbin/tini","-g","--"]  
  
CMD ["nginx", "-g", "daemon off;"]  


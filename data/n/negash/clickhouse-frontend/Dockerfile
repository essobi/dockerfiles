FROM nginx:stable-alpine  
  
ENV ALLOW_IP 0.0.0.0  
ENV DOLLAR $  
  
ADD nginx.template /etc/nginx/conf.d/default.template  
  
ADD docs /usr/share/nginx/html  
  
CMD /bin/sh -c "envsubst < /etc/nginx/conf.d/default.template >
/etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"  


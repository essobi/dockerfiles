FROM nginx  
  
COPY nginx.conf.template /etc/nginx/nginx.conf.template  
  
CMD /bin/bash -c "envsubst '\$NGINX_PORT \$HTTPS_DOMAIN \$APP_PORT' <
/etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf && cat
/etc/nginx/nginx.conf && nginx -g 'daemon off;'"  


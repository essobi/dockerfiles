FROM nginx:alpine  
  
COPY nginx.tmpl /etc/nginx/conf.d/  
  
CMD ["/bin/sh", "-c", "envsubst < /etc/nginx/conf.d/nginx.tmpl >
/etc/nginx/conf.d/default.conf && nginx -g \"daemon off;\""]  


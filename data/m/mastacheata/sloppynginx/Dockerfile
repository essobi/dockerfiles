FROM nginx:latest  
  
ADD nginx.conf /etc/nginx/  
ADD fastcgi_params /etc/nginx/  
  
RUN sed -i "s|__DOMAIN__|${DOMAIN}|g" /etc/nginx/nginx.conf && sed -i
"s|__ROOT__|${ROOT}|g" /etc/nginx/nginx.conf && sed -i
"s|__UPSTREAM__|${UPSTREAM}|g" /etc/nginx/nginx.conf


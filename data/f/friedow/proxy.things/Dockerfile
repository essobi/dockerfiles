FROM nginx  
  
COPY nginx.conf /etc/nginx/nginx.template  
  
CMD envsubst < /etc/nginx/nginx.template > /etc/nginx/nginx.conf && nginx -g
'daemon off;'


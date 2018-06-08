FROM nginx:1.13.12-alpine  
  
# Set default listen port  
ENV PLACEHOLDER_LISTEN_PORT=80  
# Copy placeholder over  
ADD placeholder.conf /etc/nginx/conf.d/placeholder.template  
  
# Substitute env variables and start nginx  
CMD ["/bin/sh", "-c", "envsubst < /etc/nginx/conf.d/placeholder.template >
/etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]  


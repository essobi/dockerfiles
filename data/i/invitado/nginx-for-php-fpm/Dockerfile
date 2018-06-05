FROM nginx:1.13-alpine  
  
# Add nginx config.  
COPY ./nginx.conf /etc/nginx/nginx.conf  
  
# Install dumb init.  
RUN apk add --update dumb-init && rm -rf /var/cache/apk/*  
  
# Add entrypoint script.  
COPY ./entrypoint.sh /tmp/entrypoint.sh  
RUN chmod 755 /tmp/entrypoint.sh  
CMD ["/tmp/entrypoint.sh"]  
  
EXPOSE 80  


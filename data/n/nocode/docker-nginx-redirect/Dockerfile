FROM nginx:alpine  
  
COPY default.conf /tmp/default.template  
COPY docker-entrypoint /usr/bin/docker-entrypoint  
  
EXPOSE 80  
CMD ["sh", "-c", "/usr/bin/docker-entrypoint"]  


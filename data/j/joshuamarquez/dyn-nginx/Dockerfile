FROM nginx:stable  
  
COPY templates /templates  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]


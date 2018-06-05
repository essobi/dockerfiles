FROM nginx:latest  
  
# add index template and ping endpoint  
COPY index.html /usr/share/nginx/html/index.html  
COPY ping.html /usr/share/nginx/html/ping.html  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  


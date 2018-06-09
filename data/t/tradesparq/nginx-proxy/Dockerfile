FROM nginx  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY proxy-conf /etc/nginx/sites-enabled  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  


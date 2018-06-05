FROM jwilder/nginx-proxy  
  
MAINTAINER rak@webeye.services  
  
ADD nginx-internal.tmpl /app/nginx.tmpl  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["forego", "start", "-r"]  
  


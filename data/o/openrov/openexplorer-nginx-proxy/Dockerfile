FROM jwilder/nginx-proxy:latest  
  
RUN mkdir -p /usr/share/nginx/html/files/  
  
ADD pages/50x.html /usr/share/nginx/html/  
ADD pages/files /usr/share/nginx/html/files/  
ADD custom.conf /etc/nginx/conf.d/custom.conf  
  
WORKDIR /app/  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["forego", "start", "-r"]


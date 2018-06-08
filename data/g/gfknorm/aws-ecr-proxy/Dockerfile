FROM nginx:alpine  
  
RUN apk add py2-pip --no-cache && \  
pip install --upgrade pip awscli  
  
ADD configs/nginx/nginx.conf.tmpl /etc/nginx/nginx.conf.tmpl  
ADD configs/nginx/ssl /etc/nginx/ssl  
  
ADD configs/entrypoint.sh /entrypoint.sh  
  
EXPOSE 80 443 5000  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  


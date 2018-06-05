FROM nginx:alpine  
  
ADD . /usr/share/nginx/html/  
  
RUN \  
mv /usr/share/nginx/html/nginx.conf /etc/nginx/ && \  
sed -i 's# var backend_server =.*# var backend_server =
window.location.protocol + "//" + window.location.host;#'
/usr/share/nginx/html/index.html  
  


FROM nginx:alpine  
  
ADD docker.nginx.conf /etc/nginx/conf.d/default.conf  
ADD fastcgi_params /etc/nginx/fastcgi_params  
ADD src/ /usr/share/nginx/html


from nginx:latest  
ADD nice2.conf /etc/nginx/conf.d/  
ADD nginx.conf /etc/nginx/  
RUN chmod -R 777 /var/log/nginx /var/cache/nginx /var/run \  
&& chgrp -R 0 /etc/nginx \  
&& chmod -R g+rwX /etc/nginx \  
&& rm /etc/nginx/conf.d/default.conf  
EXPOSE 8081  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  


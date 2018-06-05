FROM nginx:stable-alpine  
ADD https://static.ondy.me/kyleondy.com/master.tar.gz /tmp/  
RUN tar -xzf /tmp/master.tar.gz -C /usr/share/nginx/html \  
&& rm /tmp/master.tar.gz  


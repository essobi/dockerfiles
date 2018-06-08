FROM nginx:alpine  
  
COPY dist /usr/share/nginx/html  
  
EXPOSE 80  
ENV GITLAB_URL https://gitlab.com  
  
RUN echo '#!/bin/sh' > /entrypoint.sh \  
&& echo 'sed "s@##GITLAB_URL##@$GITLAB_URL@g" -i
/usr/share/nginx/html/index.html' >> /entrypoint.sh \  
&& echo 'nginx -g "daemon off;"' >> /entrypoint.sh \  
&& chmod u+x /entrypoint.sh  
  
RUN echo "server { \  
listen 80; \  
server_name localhost; \  
location / { \  
root /usr/share/nginx/html; \  
try_files \$uri \$uri/ /index.html; \  
} \  
}" > /etc/nginx/conf.d/default.conf  
  
CMD ["/entrypoint.sh"]


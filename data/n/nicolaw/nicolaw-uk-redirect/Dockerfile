FROM nginx:stable-alpine  
RUN echo 'server { listen 80; return 301 $scheme://nicolaw.uk$request_uri; }'
> /etc/nginx/conf.d/default.conf  


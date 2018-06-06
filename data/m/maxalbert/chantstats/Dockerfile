FROM nginx:alpine  
LABEL maintainer="Maximilian Albert <maximilian.albert@gmail.com>"  
RUN apk add --update bash vim && \  
rm /etc/nginx/conf.d/default.conf && \  
rm /var/log/nginx/access.log && \  
rm /var/log/nginx/error.log && \  
ln -s /shared/logs/nginx/access.log /var/log/nginx/access.log && \  
ln -s /shared/logs/nginx/error.log /var/log/nginx/error.log  
COPY chantstats.conf /etc/nginx/conf.d/chantstats.conf  
COPY htpasswd /etc/nginx/.htpasswd  


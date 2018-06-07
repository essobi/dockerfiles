FROM alpine:3.5  
EXPOSE 80  
RUN \  
apk add --update nodejs nginx && \  
adduser -D -u 1000 -g 'www' www && \  
mkdir /www && \  
chown -R www:www /var/lib/nginx && \  
chown -R www:www /www  
  
WORKDIR /app  
ADD package.json /app/  
RUN \  
npm install && \  
mkdir -p /run/nginx /etc/nginx/sites-enabled && \  
rm -r /etc/nginx/nginx.conf /etc/nginx/conf.d && \  
ln -s /app/nginx.conf /etc/nginx/nginx.conf && \  
ln -s /app/hosts.conf /etc/nginx/sites-enabled/ecs-proxy && \  
touch /app/hosts.conf  
  
CMD ["ash", "-cex", "/app/start.sh"]  
  
ADD ./ /app/  
RUN chmod -R go+r /app/invalid-service && \  
chown -R www:www /app/invalid-service  
  


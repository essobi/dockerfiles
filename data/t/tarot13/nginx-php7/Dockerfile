FROM tarot13/php7-fpm  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
RUN apk add --no-cache nginx && \  
sed 's/access_log \/var\/log\/nginx\/access\\.log main;/access_log off;/g' -i
/etc/nginx/nginx.conf && \  
sed 's/\\[::\\]:9000/127\\.0\\.0\\.1:9000/g' -i /usr/local/etc/php-fpm.d/zz-
docker.conf && \  
curl -L -O https://github.com/techotaku/docker-files/raw/master/nginx-
php7/entrypoint.sh && \  
chmod +x entrypoint.sh && \  
mv entrypoint.sh / && \  
curl -L -O https://github.com/techotaku/docker-files/raw/master/nginx-
php7/opcache-recommended.ini && \  
mv opcache-recommended.ini /usr/local/etc/php/conf.d/ && \  
mkdir -p /run/nginx  
  
EXPOSE 80/tcp  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]


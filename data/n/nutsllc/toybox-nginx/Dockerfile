FROM nginx:1.11-alpine  
MAINTAINER NutsProject,LLC  
  
RUN apk --no-cache add tar \  
&& tar czf /usr/src/nginx-default-doc.tar.gz -C /usr/share/nginx/html ./
--remove-files \  
&& tar czf /usr/src/nginx-conf.tar.gz -C /etc/nginx ./ --remove-files  
  
COPY default-fpm.conf /default-fpm.conf  
COPY docker-entrypoint-ex.sh /entrypoint-ex.sh  
  
ENTRYPOINT ["/entrypoint-ex.sh"]  


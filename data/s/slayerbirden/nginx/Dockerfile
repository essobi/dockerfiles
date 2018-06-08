FROM nginx:alpine  
  
MAINTAINER Oleg Kulik "okulik@gorillagroup.com"  
RUN apk update && apk add openssl \  
&& adduser -D -u 1000 www-data \  
&& sed -i -e "s/user.*nginx/user www-data/" /etc/nginx/nginx.conf  
  
COPY start.sh /  
  
ENTRYPOINT ["/start.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  


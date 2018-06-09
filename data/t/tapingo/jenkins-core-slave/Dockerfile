FROM alpine:3.1  
MAINTAINER Shuky Dvir <shuky@devops.co.il>  
  
RUN apk add --update redis \  
bash \  
&& rm -rf /var/cache/apk/* \  
&& sed -i 's#daemonize yes#daemonize no#i' /etc/redis.conf \  
&& sed -i 's|dev ./|dev /var/lib/redis|g' /etc/redis.conf \  
&& echo -e "# placeholder for local options\n" > /etc/redis-local.conf \  
&& echo -e "include /etc/redis-local.conf\n" >> /etc/redis.conf  
  
VOLUME ["/var/lib/redis/"]  
  
EXPOSE 6379  
ENTRYPOINT ["redis-server"]  


FROM ghost:latest  
MAINTAINER Promact Infotech <info@promactinfo.com>  
  
RUN chown -R user:user /usr/src/ghost  
  
# Add config and script to start the engine  
ADD config.js /usr/src/ghost/config.js  
  
RUN npm install -g pm2  
  
RUN apt-get update && apt-get install -y ca-certificates \  
nginx-full  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Add default conf for nginx  
ADD default.conf /etc/nginx/conf.d/default.conf  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
ADD entrypoint.sh /run-ghost.sh  
  
RUN chmod 777 /run-ghost.sh  
  
CMD ["sh","/run-ghost.sh"]  


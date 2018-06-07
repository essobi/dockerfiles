FROM node:6-alpine  
MAINTAINER Mitchell Hewes <me@mitcdh.com>  
  
RUN apk --update add \  
python \  
make \  
g++ \  
&& rm -rf /var/cache/apk/* \  
&& npm install -g screeps \  
&& adduser -S -g 'Screeps Server' -h '/screeps' screeps-srv  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
WORKDIR /screeps  
USER screeps-srv  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["screeps", "start"]  


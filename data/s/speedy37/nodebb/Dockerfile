FROM node:6-alpine  
MAINTAINER Vincent Rouille <vincent@speedy37.fr>  
  
WORKDIR /nodebb  
  
ENV NODE_ENV=production \  
daemon=false \  
silent=false  
  
RUN apk add --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing gosu \  
&& apk add --no-cache ca-certificates curl ssmtp \  
&& curl -L https://github.com/NodeBB/NodeBB/archive/v1.4.2.tar.gz | tar xz \  
&& find NodeBB-1.4.2 -maxdepth 1 -mindepth 1 -exec mv {} /nodebb + \  
&& npm install \  
&& ln -s /nodebb/nodebb /usr/local/bin/nodebb  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 4567  
VOLUME ["/nodebb/config.json", "/nodebb/public/uploads"]  
CMD ["nodebb", "start"]  


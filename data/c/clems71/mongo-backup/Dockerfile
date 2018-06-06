FROM alpine:edge  
  
WORKDIR /srv  
  
COPY package.json .  
COPY yarn.lock .  
  
RUN \  
echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
&& \  
apk add --no-cache mongodb-tools mysql-client nodejs nodejs-npm yarn lz4 && \  
yarn && \  
rm -rf /var/cache/apk/*  
  
COPY src src  
COPY test test  
  
ENTRYPOINT ["yarn"]  
CMD ["start"]  


FROM ubuntu:latest  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive PORT=2368 HOST=0.0.0.0 URL=http://localhost  
  
COPY ./confd-0.7.1-linux-amd64 /usr/bin/confd  
COPY ./docker-entrypoint.sh /  
ADD https://deb.nodesource.com/setup /tmp/setup-nodejs  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
chmod +x /usr/bin/confd && \  
bash /tmp/setup-nodejs && \  
apt-get install --no-install-recommends -qy nodejs vim && \  
npm install --global --production ghost pm2 && \  
cp /usr/lib/node_modules/ghost/config.example.js
/usr/lib/node_modules/ghost/config.js && \  
sed -i "s|'2368'|process.env.PORT|g" /usr/lib/node_modules/ghost/config.js &&
\  
sed -i "s|'2369'|process.env.PORT|g" /usr/lib/node_modules/ghost/config.js &&
\  
sed -i "s|'127.0.0.1'|process.env.HOST|g"
/usr/lib/node_modules/ghost/config.js && \  
sed -i "s|'http://my-ghost-blog.com'|process.env.URL|g"
/usr/lib/node_modules/ghost/config.js && \  
sed -i "s|'http://localhost:2368'|process.env.URL|g"
/usr/lib/node_modules/ghost/config.js && \  
sed -i "s|'http://127.0.0.1:2369'|process.env.URL|g"
/usr/lib/node_modules/ghost/config.js && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && npm cache
clean  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["ghost"]  


FROM mhart/alpine-node:7.2  
  
COPY . /srv/npm-register  
WORKDIR /srv/npm-register  
  
# Create user and group  
RUN addgroup -S register \  
&& adduser -D -S \  
-s /bin/bash \  
-h /srv/npm-register \  
-G register \  
register  
  
RUN apk --no-cache add python \  
gcc \  
make \  
g++ \  
&& npm install bcrypt \  
&& npm install \  
&& chown -R register:register . \  
&& apk del python \  
gcc \  
make \  
g++ \  
&& rm -rf /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
# Share storage volume  
ENV NPM_REGISTER_FS_DIRECTORY /data  
VOLUME /data  
  
# Start application  
EXPOSE 3000  
#USER register  
ENV NODE_ENV production  
CMD ["npm", "start"]  
  


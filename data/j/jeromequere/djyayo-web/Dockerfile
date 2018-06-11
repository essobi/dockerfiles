FROM smebberson/alpine-nginx-nodejs  
WORKDIR /usr/html/  
COPY src/web /usr/html/  
RUN npm install && \  
npm run-script build && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log


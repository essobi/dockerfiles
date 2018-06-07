FROM mwaaas/node-nginx:5.11.0-1.8.1-1  
RUN npm install -g angular-cli && npm install -g --save process-nextick-args  
  
# Fix bug https://github.com/npm/npm/issues/9863  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
  
COPY package.json /usr/packages/  
RUN cd /usr/packages/ && npm install --unsafe-perm=true  
  
ONBUILD COPY . /usr/src/app  
  
ONBUILD RUN cp -r /usr/packages/node_modules /usr/src/app/  
  
ONBUILD RUN npm install --unsafe-perm=true  
  
ONBUILD RUN ng build --prod --env=prod  
  
# configure nginx if there is a custom configuration  
ONBUILD RUN [ -f ./nginx.conf ] && cp /usr/src/app/nginx.conf
/etc/nginx/nginx.conf || echo "nginx file not found"  
  


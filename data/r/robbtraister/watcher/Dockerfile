FROM robbtraister/base  
  
RUN apk add --update --no-cache \  
nodejs \  
&& rm -rf /var/cache/apk/* \  
&& node -v  
  
WORKDIR /watcher  
  
ADD package.json ./  
RUN npm install --production  
  
ADD gulpfile.js logger.js ./  
  
WORKDIR /workdir  
  
VOLUME ./src  
  
# Use cd since WORKDIR will be /workdir/src  
CMD cd /watcher \  
&& npm start  


FROM mhart/alpine-node:8.7.0  
RUN mkdir /conf  
  
# source  
COPY . /ravel-app  
RUN cd /ravel-app && \  
echo "Installing packages..." && \  
npm install --no-optional && \  
npm cache clear --force && \  
node ./node_modules/gulp/bin/gulp.js build && \  
npm prune --production && \  
rm -rf src && \  
cd -  
  
WORKDIR /ravel-app/dist  
CMD ["node", "app.js"]  


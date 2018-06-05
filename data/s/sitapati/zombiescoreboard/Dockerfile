FROM sitapati/docker-alpine-node-python-make  
  
WORKDIR /build  
ADD . .  
  
RUN npm i \  
&& node node_modules/gulp/bin/gulp.js build  
  
EXPOSE 8666  
CMD ["node", "server.js"]  


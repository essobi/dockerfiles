FROM node:carbon  
  
ENV root /be  
  
RUN mkdir $root  
COPY . $root/  
RUN cd $root && npm install --unsafe-perm  
  
CMD "/usr/local/bin/node" "$root/server.js"  


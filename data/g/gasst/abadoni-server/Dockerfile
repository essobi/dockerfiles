FROM node:6.2.2-wheezy  
  
MAINTAINER Gaston Ndanyuzwe  
  
ENV PORT=80  
ADD . /var/abadoni-server  
  
WORKDIR /var/abadoni-server  
  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
  
RUN npm install webpack rimraf pm2 forever -g  
RUN npm install -p  
RUN npm run build:prod  
  
EXPOSE $PORT


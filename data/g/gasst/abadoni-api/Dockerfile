FROM node:6.2.2-wheezy  
  
MAINTAINER Gaston Ndanyuzwe  
  
ENV PORT=3264  
ADD . /var/abadoni-api  
  
WORKDIR /var/abadoni-api  
  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
  
RUN npm install typings rimraf pm2 -g  
RUN npm install -p  
RUN npm build  
  
EXPOSE $PORT


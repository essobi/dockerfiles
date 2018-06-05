FROM node:5.8  
RUN npm install -g webpack  
RUN npm install -g karma-cli  
RUN mkdir /app  
WORKDIR /app  
ADD package.json ./package.json  
RUN npm i  
#Fix npm + docker bug  
#https://github.com/npm/npm/issues/9863#issuecomment-246627668  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  


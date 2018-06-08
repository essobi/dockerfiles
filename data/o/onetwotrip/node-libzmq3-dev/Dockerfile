FROM node:6.7.0  
MAINTAINER avikez@gmail.com (Dmitry Shmelev)  
  
RUN apt-get update && apt-get install -y \  
libzmq3-dev \  
python-minimal  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/
./lib/utils/rename.js  
RUN npm install -g npm  
RUN npm install -g npm-cache  
RUN npm cache verify  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ENV HOME=/tmp  


FROM node:carbon  
  
RUN apt-get update && apt-get install -y autoconf automake build-essential
python-dev  
  
# install watchman  
RUN git clone -b v4.7.0 --single-branch
https://github.com/facebook/watchman.git /tmp/watchman && \  
cd /tmp/watchman && \  
./autogen.sh && \  
./configure && \  
make && make install && \  
rm -rf /tmp/watchman  
  
RUN npm i -g npm  
RUN npm i -g yarn exp  
  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app  
COPY yarn.lock /usr/src/app  
RUN yarn install  
  
COPY . /usr/src/app  
COPY ./config.js.staging /usr/src/app/config.js  
  
EXPOSE 19000-19300  
CMD exp start --no-dev --offline  


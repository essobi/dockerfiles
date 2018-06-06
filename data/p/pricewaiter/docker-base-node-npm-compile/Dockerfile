FROM mhart/alpine-node:8.11  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apk --update add python make g++ git \  
&& rm -rf /var/cache  
  
ONBUILD COPY package.json yarn.lock /usr/src/app/  
ONBUILD RUN yarn install --production && /bin/rm -rf /tmp/npm* /root/.npm
/tmp/v8* /usr/local/share/.cache/  
ONBUILD COPY . /usr/src/app  
  
CMD yarn run start  


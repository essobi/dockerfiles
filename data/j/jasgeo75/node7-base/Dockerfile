FROM node:7-alpine  
  
RUN apk add --no-cache \  
libstdc++ \  
git \  
&& apk add --no-cache --virtual .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python \  
&& yarn add gulp-install \  
&& yarn global add bower gulp node-gyp \  
&& yarn cache clean && \  
rm -rf /var/cache/apk/* /tmp/*  
# && apk del .build-deps  
  
CMD [ "node" ]  


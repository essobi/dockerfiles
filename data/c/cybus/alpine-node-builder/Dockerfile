FROM mhart/alpine-node-auto:6  
  
MAINTAINER Cornelio Hopmann <hopmann@cybus.io>  
  
RUN apk add --update git bash openssh openssl python build-base cmake
libc6-compat linux-headers \  
&& rm -rf /tmp/* /var/cache/apk/* \  
&& adduser -D -u 1000 node  
RUN npm set progress=false \  
&& npm install --no-progress node-gyp mocha webpack yarn -g \


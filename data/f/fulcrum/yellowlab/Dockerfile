FROM node:4.7  
# taken from https://github.com/jguyomard/docker-yellowlabtools, but its not
been updated  
#ENV VERSION=master  
ENV VERSION=v1.13.0  
WORKDIR /usr/src/ylt  
  
RUN npm install -g npm@latest \  
&& npm install -g node-gyp \  
&& npm install -g grunt-cli \  
&& git clone https://github.com/gmetais/YellowLabTools.git -b ${VERSION} . \  
&& npm install \  
&& grunt build  
  
EXPOSE 8383  
ENV NODE_ENV=production  
CMD ["node", "bin/server.js"]  


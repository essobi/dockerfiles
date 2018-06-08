FROM node:9-alpine  
  
RUN apk add --no-cache git ruby  
  
  
ENV SASS_BINARY_VERSION 4.7.2  
RUN apk add --no-cache --virtual .build-deps-node-sass curl \  
&& mkdir -p /node-sass \  
&& cd /node-sass \  
&& curl -fSLO --compressed "https://github.com/sass/node-
sass/releases/download/v$SASS_BINARY_VERSION/linux_musl-x64-57_binding.node" \  
&& apk del .build-deps-node-sass  
  
ENV SASS_BINARY_PATH /node-sass/linux_musl-x64-57_binding.node  
  
RUN yarn global add node-sass  
  
CMD ["node"]  


FROM risingstack/alpine:3.3-v6.2.0-3.6.0  
RUN apk update && apk add ffmpeg python-dev make g++  
  
COPY package.json /tmp/package.json  
WORKDIR /tmp  
ENV NODE_ENV=dev  
RUN npm install  
  
RUN mkdir /app  
RUN cp -a /tmp/node_modules/ /app  
  
COPY . /app  
WORKDIR /app  
  
RUN ./node_modules/.bin/typings install  
RUN NODE_ENV=production ./node_modules/.bin/webpack -p  
RUN ./node_modules/.bin/tsc  
  
ENV NODE_ENV=production  
CMD ["sh", "-c", "/env node out/server/server.js"]  


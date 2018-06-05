FROM node:alpine  
WORKDIR /app  
RUN apk --no-cache add --virtual native-deps \  
g++ gcc libgcc libstdc++ linux-headers make python && \  
npm install --quiet node-gyp -g &&\  
npm install --quiet && \  
apk del native-deps  
COPY package.json /app  
RUN npm install  
COPY . /app  
  
CMD npm run start  
EXPOSE 4000


FROM node:carbon-alpine  
COPY . /app  
WORKDIR /app  
RUN apk add --no-cache --virtual .gyp \  
python \  
make \  
g++ \  
&& npm install \  
&& apk del .gyp  
EXPOSE 80  
ENTRYPOINT [ "npm", "start"]


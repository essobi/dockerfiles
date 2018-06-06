FROM diddledan/polymer-base as builder  
RUN apk update && apk add git  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN npm install -g bower && \  
npm install -g typescript && \  
npm install && \  
cd src/public && \  
bower install --allow-root && \  
polymer build && \  
cd ../.. && \  
npm run build && \  
npm uninstall -g bower && \  
npm uninstall -g typescript && \  
rm -rf node_modules && \  
npm install --production  
  
# FINAL image  
FROM node:8-alpine  
COPY \--from=builder /usr/src/app /usr/src/app  
WORKDIR /usr/src/app  
EXPOSE 3000  
CMD [ "npm", "run", "production" ]  


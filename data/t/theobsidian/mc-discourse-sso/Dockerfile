FROM node:6-alpine  
  
ENV PORT 3000  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN \  
yarn install && \  
yarn run build && \  
rm -rf node_modules && \  
yarn install --production  
  
EXPOSE 3000  
CMD [ "yarn", "start" ]  


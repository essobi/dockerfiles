FROM mhart/alpine-node:7.4.0  
WORKDIR /app  
  
# install build tools  
RUN apk add --no-cache make gcc g++ python curl bash  
RUN npm install -g yarn@0.17.10 --quiet  
  
# install deps  
COPY package.json /app/  
COPY yarn.lock /app/  
RUN yarn install  
  
# remove un-used build tools  
RUN apk del make gcc g++ python  
  
# install app  
COPY . /app  
  
# compile app  
RUN NODE_ENV=production yarn compile  
  
EXPOSE 3000  
EXPOSE 3443  
CMD [ "yarn", "start" ]


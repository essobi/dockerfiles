######################  
### STAGE 1: Build ###  
FROM node:8-alpine as builder  
  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN rm -rf ./node_modules && yarn install && yarn build  
  
  
######################  
### STAGE 2: Setup ###  
FROM node:8-alpine  
  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app  
RUN yarn install --production  
COPY --from=builder /usr/src/app/dist/ /usr/src/app/dist/  
  
CMD npm start  


FROM node:alpine  
WORKDIR /srv/app  
COPY ./ /srv/app  
ENV NODE_ENV production  
RUN yarn install  
CMD npm start  


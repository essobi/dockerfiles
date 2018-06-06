FROM node:9-alpine  
  
RUN apk --no-cache add git  
  
ENV NODE_ENV=production  
  
RUN mkdir -p /mm  
WORKDIR /mm  
  
COPY package.json yarn.lock /mm/  
  
RUN yarn  
  
COPY src /mm/src  
  
CMD ["node", "src/index.js"]  


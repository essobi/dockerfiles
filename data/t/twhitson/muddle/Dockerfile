FROM node:9-alpine  
  
RUN apk add --update ffmpeg opus  
  
WORKDIR /app  
  
COPY package.json /app  
RUN npm install --only=production  
  
COPY . /app  
  
CMD npm run start  


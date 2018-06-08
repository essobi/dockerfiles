FROM mhart/alpine-node:8.5.0  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apk update && apk add --no-cache \  
build-base \  
g++ \  
cairo-dev \  
jpeg-dev \  
pango-dev \  
giflib-dev \  
ttf-freefont \  
fontconfig  
  
COPY package.json yarn.lock ./  
RUN yarn --production  
  
COPY . .  
CMD ["npm", "start"]  


FROM node:alpine as build_prep  
ARG TARGET=prod  
  
# Create app directory  
WORKDIR /app  
  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied where available (npm@5+)  
COPY package*.json ./  
  
# Install app dependencies (with dev deps to allow angular build running)  
RUN npm install --no-optional  
  
# Copying source code _after_ having node modules installed allows us to use
docker cache for packages installation step  
COPY . .  
  
RUN npm run build $TARGET  
  
FROM node:alpine  
WORKDIR /app  
  
COPY package*.json index.js ./  
  
RUN npm install --production --no-optional  
  
COPY \--from=build_prep /app/dist dist  
  
EXPOSE 3000  
ENTRYPOINT ["node", "index"]  


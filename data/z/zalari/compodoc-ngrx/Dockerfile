# official NodeJS LTS 8 image  
FROM node:8-alpine  
  
# create the default log folder  
RUN mkdir /app  
  
# set working dir  
WORKDIR /app  
  
# Add package.json before rest of repo for caching  
COPY package.json .  
COPY . .  
RUN npm install && npm run build && npm cache clean --force  
  
ENTRYPOINT ["node", "bin/index-cli.js"]  


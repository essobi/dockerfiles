FROM
node:8.11.2-alpine@sha256:04d1f711703472ccb4ddc6bc9835ac0bcfc8afa4389534152d137ab93c24474a  
  
#### Begin setup ####  
# Installs git  
RUN apk add --update git && rm -rf /var/cache/apk/*  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
# Startup  
ENTRYPOINT node example.js


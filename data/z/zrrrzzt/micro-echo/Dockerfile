# Setting the base to nodejs 8.9.1  
FROM
node:8.11.2-alpine@sha256:04d1f711703472ccb4ddc6bc9835ac0bcfc8afa4389534152d137ab93c24474a  
  
# Maintainer  
MAINTAINER Geir Gåsodden  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
ENV NODE_ENV production  
  
# Expose 3000  
EXPOSE 3000  
# Startup  
ENTRYPOINT npm start


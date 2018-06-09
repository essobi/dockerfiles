# Setting the base to nodejs 8.9.4  
FROM node:8.9.4-alpine  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
# Expose 3000  
EXPOSE 3000  
# Startup  
ENTRYPOINT npm start


FROM node:6  
EXPOSE 20 21 1025  
VOLUME /ftp  
  
# Set workdir  
WORKDIR /src  
  
# Copy over package.json  
COPY package.json ./  
  
# Install dependencies  
RUN npm install --silent -g yarn && yarn install  
  
# Copy over remaining sources  
COPY . ./  
  
# Transpile sources using babel  
RUN npm run build  
  
CMD npm run production  


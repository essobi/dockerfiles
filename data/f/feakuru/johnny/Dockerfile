FROM node:boron  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
# COPY package.json .  
# For npm@5 or later, copy package-lock.json as well  
COPY package.json .  
COPY package-lock.json .  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 3000  
RUN touch server.log  
RUN tail -n 0 -f *.log &  
  
CMD ["npm", "start", "&>", "server.log"]  


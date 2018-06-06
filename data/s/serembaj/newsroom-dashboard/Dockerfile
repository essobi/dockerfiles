FROM node:carbon  
  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
  
RUN chown -R $(whoami) $(npm config get prefix)/lib/node_modules  
  
RUN npm install -g --unsafe-perm @angular/cli  
  
COPY package.json .  
  
RUN npm install --only=production  
  
COPY .angular-cli.json .  
COPY . .  
  
# RUN ng build --aot -prod  
ENV APP_ID setYourAppId  
ENV MASTER_KEY setYourMasterKey  
ENV DATABASE_URI setMongoDBURI  
  
EXPOSE 80  
CMD ["npm", "start"]  


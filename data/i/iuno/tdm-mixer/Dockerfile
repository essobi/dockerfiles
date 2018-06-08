FROM node  
RUN npm install pm2 -g  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Bundle app source  
COPY MixerControl-app /usr/src/app  
  
# Install app dependencies  
RUN npm install  
RUN npm install -g @angular/cli --unsafe  
  
RUN ng build --prod --build-optimizer  
  
EXPOSE 3000  
CMD [ "pm2-docker", "npm", "--", "start" ]  


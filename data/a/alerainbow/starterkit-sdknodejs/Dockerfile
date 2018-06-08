FROM node:carbon  
  
# Environment variables  
ENV RAINBOW_HOST "sandbox.openrainbow.com"  
ENV RAINBOW_BOT_LOGIN ""  
ENV RAINBOW_BOT_PASSWORD ""  
# Create node directory  
WORKDIR /usr/src/node  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
  
RUN npm install  
RUN npm install forever  
# If you are building your code for production  
# RUN npm install --only=production  
# Bundle app source  
COPY . .  
  
# Update default router port  
RUN sed -i "s/3002/8080/g" /usr/src/node/app/config/router.json  
  
EXPOSE 8080  
CMD [ "./start.sh" ]


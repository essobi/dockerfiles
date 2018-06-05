FROM node:5  
RUN mkdir -p /agendash  
  
ADD package.json /agendash  
ADD jsconfig.json /agendash  
  
WORKDIR /agendash  
  
RUN npm install  
  
ADD index.js /agendash  
  
## ENV  
#ENV MONGODB_ADDRESS mongodb://mongo:27017/agenda  
#ENV MOUNT_PATH agendash  
EXPOSE 3000  
ENV NODE_PATH .  
  
CMD ["npm", "start"]


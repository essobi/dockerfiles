FROM node:9.3-alpine  
WORKDIR /home/node  
  
# adding package.json first, to take advantage of cached docker layers  
ADD package.json package.json  
RUN npm install --only=production && npm cache clean --force  
USER node  
  
# add the rest of the app  
COPY . .  
EXPOSE 8099  
CMD ["npm", "start"]


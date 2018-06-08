FROM node:alpine  
  
WORKDIR /flare-app-dashboard  
  
COPY . .  
RUN npm install && \  
npm run build  
  
EXPOSE 5000  
CMD npm run serve  


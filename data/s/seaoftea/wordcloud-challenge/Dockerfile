FROM node:6.10.0  
MAINTAINER Tom Constantine  
  
WORKDIR /opt/nodeapp  
  
RUN npm install -g serve  
  
COPY package.json package.json  
  
RUN yarn install  
  
COPY . .  
  
RUN yarn run build  
  
EXPOSE 5000  
CMD ["serve", "-s", "build"]  


FROM node:7-alpine  
  
WORKDIR /home/spielplan  
  
ADD package.json /home/spielplan/package.json  
RUN npm install  
  
COPY . /home/spielplan  
  
ENV PORT 80  
WORKDIR /home/spielplan  
  
EXPOSE 80  
CMD ["npm", "start"]  


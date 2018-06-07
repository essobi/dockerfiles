FROM node:latest  
  
RUN mkdir /opt/massets  
COPY ./ /opt/massets  
  
WORKDIR /opt/massets  
  
RUN npm install && npm run build  
  
EXPOSE 3000  
ENTRYPOINT ["npm", "start"]


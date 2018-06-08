FROM oyinloslos/nodebase:latest  
  
RUN mkdir -p /opt/app  
  
WORKDIR /opt/app  
  
ADD ./src /opt/app/src  
ADD ./package.json /opt/app  
  
RUN npm install  
  
EXPOSE 2000 3000  
CMD ["npm", "start"]


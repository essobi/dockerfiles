FROM flexhub/flexbox_web:latest  
  
WORKDIR /src  
WORKDIR /src  
ADD package.json package.json  
RUN npm install  
  
ADD . .  
RUN gulp  
  
EXPOSE 8080  
CMD ["npm", "run", "start"]  


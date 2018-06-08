FROM node  
WORKDIR .  
RUN mkdir /eventLogCollector  
ADD ./ /eventLogCollector/  
WORKDIR /eventLogCollector  
RUN npm install --no-optional  
EXPOSE 8000  
ENTRYPOINT ["npm", "start"]  


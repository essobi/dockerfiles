FROM node:8  
RUN mkdir /travelpack-api  
COPY . /travelpack-api  
WORKDIR /travelpack-api  
CMD ["rm", "package-lock.json"]  
RUN npm i  
EXPOSE 3030  
CMD ["npm", "start"]  


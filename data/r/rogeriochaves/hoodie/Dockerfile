FROM node:6.5.0  
COPY ./ /www  
WORKDIR www  
  
RUN npm rebuild  
RUN npm install  
  
EXPOSE 8080  
CMD ["npm", "start"]  


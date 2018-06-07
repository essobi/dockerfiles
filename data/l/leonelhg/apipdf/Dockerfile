  
FROM node:slim  
  
WORKDIR /miapp  
  
ADD . /miapp  
  
RUN npm install  
  
VOLUME /datos  
  
EXPOSE 3000  
CMD ["npm","start"]  


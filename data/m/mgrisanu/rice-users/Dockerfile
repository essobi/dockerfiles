FROM node  
  
RUN mkdir /src  
  
WORKDIR /src  
COPY . /src  
  
RUN npm install -q  
  
EXPOSE 3001  
CMD ["npm", "run", "start_prod"]


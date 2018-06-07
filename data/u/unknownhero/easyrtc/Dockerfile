FROM unknownhero/ubuntu-node-n  
  
RUN n latest  
  
# Bundle app source  
COPY ./app/package.json /src/app/package.json  
  
WORKDIR /src/app  
  
RUN npm install --no-bin-links  
  
COPY . /src  
  
EXPOSE 47121  
CMD ["node","server.js"]  


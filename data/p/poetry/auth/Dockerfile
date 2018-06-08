FROM node  
  
WORKDIR /var/app  
RUN npm i -g babel-cli  
  
COPY ./package.json /var/app/package.json  
RUN npm install  
  
COPY . /var/app  
  
EXPOSE 8000  
ENTRYPOINT exec npm start  


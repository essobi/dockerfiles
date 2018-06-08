FROM node:latest  
  
RUN mkdir /src  
  
RUN npm install nodemon -g  
  
WORKDIR /src  
ADD . /src  
RUN npm install  
COPY ./public/ /src  
  
EXPOSE 3000  
CMD npm start  


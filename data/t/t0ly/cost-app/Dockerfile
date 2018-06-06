FROM node:boron  
#FROM node:4-onbuild  
RUN mkdir -p /src  
  
#ADD . /app  
COPY . /src  
  
WORKDIR /src  
  
RUN npm install  
  
CMD node bin/www  
#COPY . /app  
EXPOSE 8081  
#RUN ["npm", "install"]  
#RUN ["npm", "run", "build"]  
#CMD ["npm", "run", "start"]  


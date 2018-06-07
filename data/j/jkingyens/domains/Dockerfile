FROM node:6  
WORKDIR /usr/src  
COPY . /usr/src  
RUN npm install  
RUN npm run build  
RUN npm install -g serve  
CMD [ "serve", "-s", "build" ]  
EXPOSE 5000  


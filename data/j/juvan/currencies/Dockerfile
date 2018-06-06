FROM node:4  
# replace this with your application's default port  
ADD . /www  
WORKDIR /www  
# install your application's dependencies  
RUN npm install  
EXPOSE 3000  
# replace this with your startup command  
CMD [ "node", "index.js" ]  


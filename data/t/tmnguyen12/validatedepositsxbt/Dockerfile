# specify the node base image with your desired version node:<version>  
FROM node:10  
RUN mkdir /validatedepositsxbt  
ADD . /validatedepositsxbt  
WORKDIR /validatedepositsxbt  
  
RUN npm i  
  
# replace this with your application's default port  
CMD ["npm", "start"]  


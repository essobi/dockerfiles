#OCKER-VERSION 0.10.0  
#FROM ubuntu:trusty  
FROM node:4-onbuild  
#FROM ubuntu:13.10  
# make sure apt is up to date  
RUN apt-get update  
  
# install nodejs and npm  
RUN apt-get install -y nodejs npm node  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY package.json /app/  
RUN npm install  
  
COPY . /app/  
  
#CMD ["/bin/bash"]  
EXPOSE 3000  
CMD ["node", "app.js"]  


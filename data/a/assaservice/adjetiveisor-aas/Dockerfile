# Sorry people of teh Internets, I need to put some dox here.  
# To start the Docker do something like: docker run --name adjetiveisor-aas -p
127.0.0.1:8000:8000 -d assaservice/adjetiveisor-aas  
#Then configure nginx and well like restart it or reload it and do your very
best with this. It's just awesome.  
FROM node:6.11.5  
MAINTAINER Axel Amigo <adamigo@neversyn.com>  
  
#Define the environment variables  
ENV SERVER_PORT=8000  
#Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
#Install the sexy dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source (this is not a sexy process)  
COPY . /usr/src/app  
  
EXPOSE ${SERVER_PORT}  
  
CMD [ "npm", "start" ]  


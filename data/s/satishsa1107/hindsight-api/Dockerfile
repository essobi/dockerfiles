FROM ubuntu  
RUN apt-get update  
RUN apt-get -y install bash git openssh-client g++ gcc libc6-dev make curl
sudo  
  
RUN curl --silent --location https://deb.nodesource.com/setup_4.x | sudo bash
-  
RUN apt-get -y install nodejs python  
RUN npm install -g npm@2.7.6  
  
WORKDIR /app  
  
ADD . /app  
RUN npm install  
EXPOSE 3001  
EXPOSE 3002  
RUN cat /app/node_modules/hindsight-core/src/domains/mentor/index.js  
  
RUN npm run build  
CMD ["node", "./lib"]  
  


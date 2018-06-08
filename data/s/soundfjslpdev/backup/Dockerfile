FROM dtanakax/nodejs  
  
RUN apt-get update && \  
apt-get -y install make python gcc build-essential mongodb-clients && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
  
RUN npm install  
  
COPY . /usr/src/app  
  
EXPOSE 8888  
CMD ["node", "app"]  
  


FROM jpetazzo/dind  
  
FROM jpetazzo/dind  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 2329  
EXPOSE 3000  
RUN chmod +x ./volume/execute.sh  
  
ENTRYPOINT service docker start && npm start && ./volume/execute.sh  
  


#  
# ThisissoonFM Sockets  
# Builds a docker image to run the node socket server for thisissoon.fm  
#  
FROM google/nodejs:0.10.33  
# Install global dependencies  
RUN npm install -g forever \  
grunt-cli  
  
# Install app dependencies  
WORKDIR /fm  
ADD package.json /fm/package.json  
RUN npm install  
  
# Bundle app source  
ADD . /fm  
  
EXPOSE 8080  
CMD ["npm", "start"]  


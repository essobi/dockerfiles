FROM ubuntu  
EXPOSE 8080  
RUN apt-get update  
RUN apt-get install -y nodejs npm nodejs-legacy  
  
# Install app dependencies  
COPY src/package.json /package.json  
RUN cd /src; npm install  
  
# Bundle app source  
COPY . /src  
  
EXPOSE 8080  
RUN npm install mongodb --save  
RUN npm install --save body-parser  
RUN npm install --save bcrypt  
RUN npm install request --save  
RUN npm install http --save  
RUN npm install querystring --save  
CMD ["bash", "/src/init.sh"]  


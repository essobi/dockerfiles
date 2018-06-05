FROM centos:centos6  
  
RUN yum install -y epel-release  
RUN yum install -y nodejs npm  
  
COPY package.json /GaultMillau/package.json  
  
# Set the working directory  
WORKDIR /GaultMillau  
  
RUN npm install --production  
  
COPY . /GaultMillau  
  
EXPOSE 8080  
CMD ["npm", "start"]


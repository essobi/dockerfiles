FROM centos:centos6  
  
# Enable Extra Packages for Enterprise Linux (EPEL) for CentOS  
RUN yum install -y epel-release  
# Install Node.js and npm  
RUN yum install -y nodejs npm git  
RUN npm install bower -g  
  
# Install app dependencies  
COPY package.json /src/package.json  
RUN cd /src; npm install  
  
# Bundle app source  
COPY . /src  
  
RUN npm update && bower update --allow-root  
  
RUN cd /src; bower install --allow-root  
  
EXPOSE 80  
CMD ["node", "/src/app.js"]  


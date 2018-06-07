FROM centos:latest  
  
# Enable Extra Packages for Enterprise Linux (EPEL) for CentOS  
RUN yum install epel-release -y  
# Install Node.js and npm  
RUN yum install nodejs npm -y  
  
# Install app dependencies  
COPY src/package.json /src/package.json  
RUN cd /src; npm install  
  
# Bundle app source  
COPY /src/. /src  
  
EXPOSE 3000  
CMD ["node", "/src/app.js"]  


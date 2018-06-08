#Builds nodemon and forever onto a centOS image  
#(Along with NPM, of course)  
FROM centos:centos7  
  
RUN yum install -y gcc gcc-c++  
RUN curl https://nodejs.org/dist/v5.3.0/node-v5.3.0-linux-x64.tar.gz >
node-v5.3.0-linux-x64.tar.gz  
RUN tar --strip-components 1 -xzvf node-v* -C /usr/local  
RUN rm -r node-v*  
RUN yum autoremove -y gcc gcc-c++  
  
RUN npm install -g inherits  
RUN npm install -g nodemon forever  


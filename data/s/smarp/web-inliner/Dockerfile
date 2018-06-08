FROM node:5.1.0  
# Enable Extra Packages for Enterprise Linux (EPEL) for CentOS  
#RUN yum install -y epel-release  
#RUN yum install -y git  
# Install Node.js and npm  
#RUN yum install -y nodejs npm  
# Install app dependencies  
COPY package.json /src/package.json  
RUN cd /src; npm install  
COPY . /src  
ENV MS_INLINER_ADDRESS 0.0.0.0  
ENV MS_INLINER_HTTP_PORT 18765  
ENV MS_INLINER_TCP_PORT 17654  
ENV MS_INLINER_METHOD=inline  
EXPOSE 17654 18765  
CMD ["node", "/src/src/inline.js"]


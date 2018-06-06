FROM centos:centos6  
RUN yum install -y epel-release  
RUN yum install -y nodejs npm && mkdir /src  
COPY package.json /src/  
RUN cd /src; npm install  
COPY index.js /src/  
EXPOSE 8080  
CMD ["node", "/src/index.js"]  


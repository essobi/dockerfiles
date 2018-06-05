FROM centos:centos6  
RUN yum install -y wget tar xz  
RUN wget https://nodejs.org/dist/v4.2.6/node-v4.2.6-linux-x64.tar.xz  
RUN tar xvf node-v4.2.6-linux-x64.tar.xz -C /opt  
COPY src /srv/  
COPY package.json /srv/  
RUN cd /srv; /opt/node-v4.2.6-linux-x64/bin/npm install  
EXPOSE 3000  
CMD ["/opt/node-v4.2.6-linux-x64/bin/node","/srv/index.js"]  


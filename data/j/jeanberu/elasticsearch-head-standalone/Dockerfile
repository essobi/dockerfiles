FROM node:slim  
  
RUN apt-get update && \  
apt-get install -y git node-gyp && \  
apt-get autoremove -y && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* && \  
npm install -g grunt grunt-cli && \  
git clone git://github.com/mobz/elasticsearch-head.git  
  
RUN cd elasticsearch-head && \  
npm install && \  
sed -i 's/port: 9100,/hostname: "0.0.0.0", port: 9100,/g' Gruntfile.js  
  
WORKDIR /elasticsearch-head  
  
EXPOSE 9100  
CMD ["grunt", "server"]  


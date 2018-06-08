FROM node  
  
WORKDIR /root  
  
COPY package.json /root/  
COPY config/* /root/config/  
COPY CHANGES.md /root/  
COPY godlive.js /root/  
  
RUN npm install  
  
ENTRYPOINT /usr/local/bin/node godlive.js  


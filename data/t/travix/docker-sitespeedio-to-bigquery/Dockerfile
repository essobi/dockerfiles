FROM sitespeedio/sitespeed.io:4.3.7  
RUN mkdir -p /root/app/tasks  
  
COPY package.json /root/app  
COPY tasks /root/app/tasks  
  
RUN cd /root/app && npm install  


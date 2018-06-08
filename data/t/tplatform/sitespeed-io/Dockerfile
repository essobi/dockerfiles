FROM sitespeedio/sitespeed.io:4.7.0  
COPY plugins/ /usr/src/app/lib/plugins/  
RUN ls -la /usr/src/app/lib/plugins/  
  
WORKDIR /usr/src/app  
# jsdom 9.12.0 is the last supported by node below v6  
RUN npm install jsdom@9.12.0 yslow@3.1.0 --save  
  
WORKDIR /sitespeed.io  


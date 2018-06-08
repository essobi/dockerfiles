FROM reelevant/docker-node-infinality  
  
WORKDIR /src  
  
ENV HOME /src  
  
EXPOSE 3000  
ADD . /src  
  
RUN npm install  
RUN npm rebuild phantomjs-prebuilt  
RUN npm install pm2 -g  
  
CMD ["pm2-docker", "/src/index.js"]  
  


FROM vansteki/daily-docker  
ADD . /opt/app  
WORKDIR /opt/app  
RUN npm install  
VOLUME ['/data']  
CMD ["node", "app.js"]  


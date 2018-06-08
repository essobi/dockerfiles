FROM node  
  
RUN npm install -g bower  
  
COPY entrypoint.sh /  
  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  


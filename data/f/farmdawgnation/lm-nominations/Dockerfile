FROM node:6.11.1  
ADD . /opt/lm-nominations  
  
WORKDIR /opt/lm-nominations  
  
RUN npm install  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
  
RUN chmod +x /usr/local/bin/dumb-init  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
  
CMD ["node", "app.js"]  


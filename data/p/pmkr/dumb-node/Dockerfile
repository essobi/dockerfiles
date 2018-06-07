FROM node:10.3.0-alpine  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64 /usr/local/bin/dumb-init  
  
RUN chmod +x /usr/local/bin/dumb-init  
  
ENTRYPOINT [ "dumb-init", "--" ]  
  
CMD [ "node" ]  


FROM node:8.3.0  
RUN npm install --global gatsby-cli@1.0.9  
RUN gatsby build --help  
  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  


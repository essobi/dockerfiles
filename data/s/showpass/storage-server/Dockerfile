FROM node:argon  
  
RUN npm install http-server -g  
  
WORKDIR /home/  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  


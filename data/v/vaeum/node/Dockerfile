FROM node:8  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["npm", "start"]  


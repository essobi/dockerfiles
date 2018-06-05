FROM node:alpine  
  
VOLUME /mnt  
WORKDIR /mnt  
  
RUN npm install -g emojipacks  
  
ENTRYPOINT ["emojipacks"]  
CMD ["--help"]  


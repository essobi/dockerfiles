FROM node:8  
EXPOSE 4567  
VOLUME /var/lib/kinesalite  
ENV PATH=$PATH:/node_modules/.bin  
RUN npm install kinesalite  
CMD ["kinesalite", "--path", "/var/lib/kinesalite"]  


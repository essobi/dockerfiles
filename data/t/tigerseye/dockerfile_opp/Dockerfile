FROM node:6  
RUN npm install pm2 -g  
ADD data /data  
ADD startup.sh /  
RUN chmod a+x /startup.sh  
EXPOSE 3000  
VOLUME ["/app"]  
WORKDIR /app  
CMD ["/startup.sh"]  
  


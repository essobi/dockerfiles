FROM node:0.12  
  
ENV PORT 3000  
ENV DIR /data  
  
RUN mkdir /data  
RUN npm install http-server -g  
  
EXPOSE 3000  
  
CMD http-server $DIR -p $PORT  


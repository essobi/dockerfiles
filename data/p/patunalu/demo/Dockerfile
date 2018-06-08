#This image is built on runtime and is used for test  
FROM patunalu/node-alpine  
LABEL maintainer="Don Peter C. Atunalu <peter@donpeter.me>" \  
application="RTConn"  
#Set enviroment to production  
ENV NODE_ENV=test  
  
#Copy build.sh to /usr/local/bin and make it executable  
COPY docker/test/build.sh /usr/local/bin/build.sh  
RUN chmod +x /usr/local/bin/build.sh  
  
#Copy the src to application and make it the workig director  
COPY src /app  
WORKDIR /app  
#USER node  
ENTRYPOINT ["build.sh"]  
CMD ["npm", "test"]  


FROM mhart/alpine-node  
  
LABEL maintainer "philip.martzok@gmail.com"  
  
RUN npm install --global azure-cli  
  
ADD bin/mongorestore /  
RUN chmod 0755 /mongorestore  
  
ADD restore.sh /  
RUN chmod 0755 restore.sh  
  
ENTRYPOINT ["/restore.sh"]  


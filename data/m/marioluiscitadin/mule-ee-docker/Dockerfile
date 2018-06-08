FROM node:6  
MAINTAINER cpswan  
  
# install node-red  
RUN npm install -g node-red  
  
# expose port  
EXPOSE 1880  
# Define mount points.  
#VOLUME ["/usr/local/bin/node-red"]  
VOLUME ["/root/.node-red"]  
  
ADD App /root/.node-red  
CMD ECHO "AFTER ADDING FILES"  
CMD ls  
  
CMD ["/usr/local/bin/node-red"]  


FROM node  
# install node-red  
RUN npm install -g node-red  
# install other nodes  
RUN npm install -g \  
node-red-node-mongodb \  
node-red-node-mysql  
# expose port  
EXPOSE 1880  
  
ADD settings.js /usr/local/lib/node_modules/node-red/  
ADD start.sh /root/  
  
# Set the default command to execute  
# when creating a new container  
# CMD ["/usr/local/bin/node-red"]  
CMD ["/root/start.sh"]  
  


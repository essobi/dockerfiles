FROM node:4  
RUN groupadd -r red && useradd -m -r -g red red  
RUN chown -R red $(npm config get prefix)/*  
USER red  
RUN npm install -g node-red && mkdir -p /home/red/.node-red && mkdir -p
/home/red/.node-red-contrib-hangouts  
  
WORKDIR /home/red/.node-red  
  
RUN ls -la /home/red  
  
RUN npm install node-red-contrib-owfs node-red-contrib-elasticsearch node-red-
contrib-hangouts sonos  
ADD settings.js /home/red/.node-red/settings.js  
  
# expose port  
EXPOSE 1880  
VOLUME /home/red/.node-red  
VOLUME /home/red/.node-red-contrib-hangouts  
  
# Set the default command to execute  
# when creating a new container  
CMD ["node-red"]  


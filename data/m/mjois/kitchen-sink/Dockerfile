FROM node:slim  
MAINTAINER Manny Jois <m.k.jois@gmail.com>  
  
WORKDIR /opt/kitchen-sink  
COPY . .  
  
RUN \  
cp scripts/docker/init /usr/sbin/my_init && \  
npm install --production && \  
npm cache clear && \  
scripts/docker/imclean  
  
EXPOSE 5056  
ENTRYPOINT ["/usr/sbin/my_init"]  
CMD ["node", "lib/server.js"]  


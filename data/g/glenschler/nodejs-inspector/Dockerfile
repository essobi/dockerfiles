# do not get FROM :onbuild because, this is just a base image of  
# node and node-inspector. Not intended to be an image holding application
files  
FROM node:0.10  
  
RUN npm install -g node-inspector  
# setup the workdir  
WORKDIR /opt/app/node  
RUN cd /opt/app/node  
# the node-inspector web host port  
EXPOSE 8080  
  
ENTRYPOINT ["node-debug", "--web-host", "0.0.0.0", "--cli", "true"]  
  
# These are default parameters which can be overridden at run time  
CMD ["./index.js"]  


FROM mhart/alpine-node:5.11  
WORKDIR /src  
  
# http://bit.ly/1QfnlUR  
ADD package.json /tmp/package.json  
RUN cd /tmp && NODE_ENV=production npm install  
RUN cp -a /tmp/node_modules /src/node_modules  
  
ADD . .  
  
EXPOSE 3000  
CMD ["npm", "start"]  


FROM node:0.12  
  
RUN npm install -g mocha coffee-script chakram  
  
ENV NODE_PATH /usr/local/lib/node_modules  
  
ENTRYPOINT ["mocha", "--compilers", "coffee:coffee-script/register"]  


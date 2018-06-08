FROM node:4.4  
ADD package.json /  
ADD external-scripts.json /  
RUN npm install  
ENV PATH $PATH:/node_modules/.bin  
CMD [ "node_modules/.bin/hubot", "-a", "slack" ]  


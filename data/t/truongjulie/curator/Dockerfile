FROM nodesource/trusty:6.2.2  
ADD package.json package.json  
RUN npm install  
RUN npm install forever -g  
ADD . .  
  
CMD ["npm", "start"]


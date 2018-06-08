FROM node  
  
WORKDIR /opt/gasconade  
ADD . /opt/gasconade  
RUN npm install  
RUN node_modules/.bin/bower --allow-root install  
  
EXPOSE 3000  
CMD ["npm", "start"]


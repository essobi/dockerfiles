  
FROM node  
  
WORKDIR /home/audit-ready-service  
  
ADD package.json /home/audit-ready-service/package.json  
RUN npm install  
  
# Make everything available for start  
ADD . /home/audit-ready-service  
  
EXPOSE 3000  
CMD ["node","server.js"]


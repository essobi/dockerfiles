FROM node:8.4.0  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY ./EmployeeDB/ ./  
RUN npm install  
CMD ["node", "app.js"]  


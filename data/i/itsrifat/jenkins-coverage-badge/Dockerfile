FROM node  
  
COPY . /opt/jenkins-coverage-badge  
  
WORKDIR /opt/jenkins-coverage-badge  
  
RUN npm install  
  
EXPOSE 9913  
CMD ["node","server.js"]  


FROM node:latest  
  
# COMMIT PROJECT FILES  
ADD package.json /root/  
ADD test.js /root/  
ADD app.js /root/  
  
# INSTALL PROJECT DEPENDENCIES  
RUN cd /root; npm install  
  
# TEST THE PROJECT -- FAILURE WILL HALT IMAGE CREATION  
RUN cd /root; npm test  
  
# TESTS PASSED -- CONFIGURE IMAGE  
WORKDIR /root  
CMD ["npm", "start"]  
EXPOSE 8080  


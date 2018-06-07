FROM hcastermans/iot-node-base  
MAINTAINER henk-jan.castermans@itility.nl  
  
# Adding source files into container  
ADD src/ /src  
  
# Define working directory  
WORKDIR /src  
  
# Open Port 80  
EXPOSE 80  
# Run Node.js  
CMD ["node", "index.js"]  


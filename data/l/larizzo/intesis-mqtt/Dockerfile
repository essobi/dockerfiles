FROM node:alpine  
MAINTAINER Bradley Scott  
  
# Copy code to container  
RUN mkdir intesis_mqtt  
COPY . /intesis_mqtt  
  
# Get dependencies  
RUN cd intesis_mqtt \  
&& npm install  
  
# Define working directory.  
WORKDIR /intesis_mqtt  
  
# Start the service  
CMD npm start  


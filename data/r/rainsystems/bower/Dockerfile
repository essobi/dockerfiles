FROM node:5-slim  
RUN npm install -g bower@1.7.2  
# Used by bower for github packages  
RUN apt-get update && apt-get install -y git  
RUN mkdir /app  
WORKDIR /app  
ENTRYPOINT ["/bower"]  


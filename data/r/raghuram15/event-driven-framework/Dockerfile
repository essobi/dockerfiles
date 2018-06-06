# Import nodejs boron version  
FROM node:boron  
# Create a new directory  
RUN mkdir -p /usr/src/Event\ Driven\ Framework/  
# Change Working Directory  
WORKDIR /usr/src/Event\ Driven\ Framework/  
# Install app dependencies  
RUN npm install  
RUN curl https://get.dgraph.io -sSf | bash  
# Port expose  
EXPOSE 8080  
#Run the final Related Files and show output  
CMD [ "node" , "npm" , "start" ]  


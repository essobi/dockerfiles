FROM node:latest  
  
# Create the working directory  
RUN mkdir -p /usr/src/spyfone  
WORKDIR /usr/src/spyfone  
  
# Pass and install dependencies  
COPY package.json /usr/src/spyfone  
RUN npm install  
  
# Take the whole app into the created directory  
COPY . /usr/src/spyfone  
  
# Expose the port that it is going to be used, our case 8080  
EXPOSE 8080  
# Execute the app  
CMD ["npm", "start"]  


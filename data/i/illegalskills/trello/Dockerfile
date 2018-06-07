# Create image based on the official Node 6 image from dockerhub  
FROM node  
  
# Create a directory where our app will be placed  
#RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/app -p /usr/src/node_modules  
ENV NODE_PATH=/usr/src/node_modules  
  
# Change directory so that our commands run inside this new directory  
WORKDIR /usr/src/app  
  
# Copy dependency definitions  
#COPY package.json /usr/src/app  
COPY package.json ./package.json  
  
# Install dependecies  
RUN npm install  
  
# Get all the code needed to run the app  
COPY . /usr/src/app  
  
# Expose the port the app runs in  
EXPOSE 4200  
# Serve the app  
CMD ["npm", "start"]


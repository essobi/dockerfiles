# Use an official Node runtime as a parent image  
FROM node:carbon  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
COPY package*.json ./  
  
RUN npm install  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
# Make port 9000 available to the world outside this container  
EXPOSE 9000  
# Define environment variable  
ENV NAME World  
  
# Run app.py when the container launches  
CMD ["npm", "start"]


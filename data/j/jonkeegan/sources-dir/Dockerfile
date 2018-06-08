# Use an official Python runtime as a parent image  
FROM node:boron  
  
# Set the working directory to /app  
WORKDIR /src  
  
# Install app dependencies  
COPY package.json .  
  
RUN npm install  
  
# Bundle app source  
COPY . .  
  
# Make port 80 available to the world outside this container  
EXPOSE 3000  
# Run app.py when the container launches  
CMD [ "npm", "start" ]  


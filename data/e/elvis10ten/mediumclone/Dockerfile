# Set the base image  
FROM node:carbon  
  
# An environment variable for the project directory  
ENV PROJECT_DIRECTORY /app  
  
# Create the project directory  
RUN mkdir ${PROJECT_DIRECTORY}  
  
# Set the working directory  
WORKDIR ${PROJECT_DIRECTORY}  
  
# Install app dependencies  
# A wildcard is used to ensure that package.json and package-lock.json are
both copied were available  
COPY package*.json ./  
  
RUN npm install  
  
# Copy the project files into the working directory  
COPY . .  
  
EXPOSE 8080  
CMD ["npm", "start"]


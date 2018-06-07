# Start with an image with Node.js pre-installed  
FROM jakewalker/nodejs  
  
RUN apt-get update  
  
# Install `build`  
RUN apt-get install build-essential -y  
  
# Copy the application to the container  
COPY index.js /opt/index.js  
COPY package.json /opt/package.json  
COPY robot.png /opt/robot.png  
  
# Set the working directory to the application folder  
WORKDIR /opt/  
  
# Install all the required libraries  
RUN npm install  
  
ENV BOT_TOKEN="REQUIRED"  
# Set the entry point  
CMD ["node", "index.js"]  


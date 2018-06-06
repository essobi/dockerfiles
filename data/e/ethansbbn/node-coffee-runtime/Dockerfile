FROM ethansbbn/node-base:0.12.0  
RUN npm install coffee-script -g  
  
# Set current working directory to /app  
WORKDIR /app  
# Copy package.json to /app/  
ONBUILD ADD package.json /app/  
# Install dependencies  
ONBUILD RUN npm install  
  
# Copy the app source coffescript files  
ONBUILD ADD src /app/src/  
# Compile source  
ONBUILD RUN coffee --compile --output /app/ /app/src/


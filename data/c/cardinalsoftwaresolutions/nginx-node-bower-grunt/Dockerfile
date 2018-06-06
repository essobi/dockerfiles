#Last Updated 4/21/16  
FROM nginx  
  
# Download packages  
RUN apt-get update && apt-get install -y git nodejs npm  
  
# Create a symbolic link for node, as many Node.js tools use this name to
execute  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install bower & grunt-cli  
RUN npm install -g bower grunt-cli


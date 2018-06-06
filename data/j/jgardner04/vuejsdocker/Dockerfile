# Image for node LTS  
FROM node  
  
# Create app directory  
WORKDIR /app  
  
# Install Yarn you can skip this if you are using NPM  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  
  
# Install app dependencies  
COPY package*.json ./  
RUN yarn  
  
# run NPM install if you are using NPM and comment out the Yarn command  
# Set the process.env.host variable to enable routing to the docker container  
ENV HOST=0.0.0.0  
# Expose the port for the Vuejs server  
EXPOSE 8080  
# Expose the port for node inspect  
EXPOSE 9229  
# Set the command to run at container start. Change this to CMD ["npm", "dev"]
if you are using npm.  
CMD ["yarn", "serve" ]  


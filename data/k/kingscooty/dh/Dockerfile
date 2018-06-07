FROM node:0.12.2  
# Set env here to avoid  
# ENV NODE_ENV=production  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install --production  
COPY . /usr/src/app  
  
# Install bower  
RUN npm install -g bower # grunt-cli  
  
# WORKDIR src/app  
RUN bower install --allow-root  
  
# Expose port  
EXPOSE 3000  
# Run app using nodemon  
CMD ["npm", "start"]  


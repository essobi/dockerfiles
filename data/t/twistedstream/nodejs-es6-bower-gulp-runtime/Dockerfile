FROM node:0.11-onbuild  
MAINTAINER twistedstream  
  
# Install Bower & Gulp  
RUN npm install -g bower gulp  
  
# Set instructions on build.  
ONBUILD ADD package.json /app/  
ONBUILD RUN npm install  
ONBUILD ADD bower.json .bowerrc /app/  
ONBUILD RUN bower install --allow-root  
ONBUILD ADD . /app  
ONBUILD RUN gulp build  
  
# Define working directory.  
WORKDIR /app  
  
# Set environment  
ENV PORT 8080  
# Define default command.  
CMD ["npm", "start"]  
  
EXPOSE 8080  


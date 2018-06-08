FROM node:8.2.0-alpine  
MAINTAINER Sean Marciniak <seanmarciniak@gmail.com>  
  
# Setting the website directory as a enviroment variable.  
# This is so it can used within the system.  
ENV WEBSITE_DIR /home/website  
# Setting the app's enviroment to be production so errors are  
# not verbose.  
ENV env production  
  
  
RUN addgroup -S website && adduser -S -g website website  
  
USER website  
  
#Copy all the content that is being used for the website  
COPY . ${WEBSITE_DIR}  
  
# Setting the current directory to be the website application  
WORKDIR ${WEBSITE_DIR}  
  
RUN npm install  
  
# Command to run on start up  
CMD npm start  


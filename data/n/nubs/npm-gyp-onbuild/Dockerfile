FROM nubs/npm-gyp-build:latest  
  
MAINTAINER Spencer Rinehart <anubis@overthemonkey.com>  
  
# Add the project code to the correct spot  
ONBUILD ADD . /code  
  
# Install the dependencies  
ONBUILD RUN npm install  
  
# Override npm install CMD with one to execute the project  
CMD ["npm", "start"]  


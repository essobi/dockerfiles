FROM node:5  
MAINTAINER Ray Tran <ray@artran.co.uk>  
  
RUN npm install -g karma jasmine-core requirejs phantomjs-prebuilt karma-
phantomjs-launcher karma-jasmine karma-requirejs  
  
CMD ["echo", "Usage: docker run --rm -v \$(pwd):/tmp/sources artran/karma
/tmp/sources karma-ci.conf.js"]  


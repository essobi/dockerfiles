FROM node:6  
EXPOSE 8000  
EXPOSE 8080  
MAINTAINER Jean-Christophe Hoelt <hoelt@fovea.cc>  
RUN useradd app -d /home/app  
WORKDIR /home/app/code  
  
COPY package.json /home/app/code/package.json  
RUN npm install  
  
COPY .snyk .eslintrc .eslintignore coffeelint.json Makefile index.js config.js
newrelic.js /home/app/code/  
COPY tests /home/app/code/tests  
COPY src /home/app/code/src  
  
RUN npm test && chown -R app /home/app  
USER app  
  
ENV API_SECRET=abcd  
  
CMD node_modules/.bin/forever index.js  


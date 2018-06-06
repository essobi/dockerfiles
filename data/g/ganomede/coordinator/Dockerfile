FROM node:6-slim  
  
EXPOSE 8000  
MAINTAINER Jean-Christophe Hoelt <hoelt@fovea.cc>  
  
# Create 'app' user  
RUN useradd app -d /home/app  
  
# Install NPM packages  
COPY package.json /home/app/code/package.json  
RUN cd /home/app/code && npm install  
  
# Copy app source files  
COPY .eslintrc .eslintignore coffeelint.json Makefile index.js config.js
newrelic.js run_tests.sh /home/app/code/  
COPY tests /home/app/code/tests  
COPY src /home/app/code/src  
RUN chown -R app /home/app  
  
USER app  
WORKDIR /home/app/code  
CMD node index.js  
  
ENV API_SECRET=1234  
ENV NODE_ENV=production  


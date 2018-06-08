# Stick to node:7 until https://github.com/restify/node-restify/issues/1374 is
fixed  
# (restify getHeaders infinite call stack)  
FROM node:7-slim  
  
EXPOSE 8000  
MAINTAINER Jean-Christophe Hoelt <hoelt@fovea.cc>  
  
# Create 'app' user  
RUN useradd app -d /home/app  
  
# Install NPM packages  
COPY package.json /home/app/code/package.json  
WORKDIR /home/app/code  
RUN npm install  
  
# Copy app source files  
COPY config.js index.js newrelic.js coffeelint.json .eslintignore .eslintrc
push-worker.sh /home/app/code/  
COPY index.js /home/app/code/index.js  
COPY index.fix.js /home/app/code/index.fix.js  
COPY tests /home/app/code/tests  
COPY src /home/app/code/src  
RUN chown -R app /home/app  
  
USER app  
CMD node index.js  
  
ENV NODE_ENV=production  


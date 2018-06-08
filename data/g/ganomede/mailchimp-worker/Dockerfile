FROM node:6-slim  
  
EXPOSE 8000  
MAINTAINER Jean-Christophe Hoelt <hoelt@fovea.cc>  
  
# Create 'app' user  
RUN useradd app -d /home/app  
WORKDIR /home/app/code  
  
# Install NPM packages  
COPY package.json /home/app/code/package.json  
RUN chown -R app /home/app  
RUN npm install  
  
# Copy app source files  
COPY index.js config.js newrelic.js .eslintrc run-tests /home/app/code/  
  
COPY tests /home/app/code/tests  
COPY src /home/app/code/src  
RUN chown -R app /home/app  
  
USER app  
WORKDIR /home/app/code  
CMD node index.js  
  
ENV NODE_ENV=production  


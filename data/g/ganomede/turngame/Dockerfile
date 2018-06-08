FROM node:6  
EXPOSE 8000  
MAINTAINER Jean-Christophe Hoelt <hoelt@fovea.cc>  
  
RUN useradd app -d /home/app  
WORKDIR /home/app/code  
  
COPY package.json /home/app/code/package.json  
RUN npm install  
  
COPY .eslintrc .eslintignore config.js coffeelint.json newrelic.js Makefile
index.js /home/app/code/  
COPY tests /home/app/code/tests  
COPY src /home/app/code/src  
  
RUN chown -R app /home/app  
USER app  
  
CMD node index.js  


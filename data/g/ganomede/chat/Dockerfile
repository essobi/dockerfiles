FROM node:6  
EXPOSE 8000  
MAINTAINER Jean-Christophe Hoelt <hoelt@fovea.cc>  
RUN useradd app -d /home/app  
WORKDIR /home/app/code  
COPY package.json /home/app/code/package.json  
RUN chown -R app /home/app  
  
USER app  
RUN npm install  
  
COPY Makefile config.js index.js newrelic.js coffeelint.json .eslintignore
.eslintrc index.js /home/app/code/  
COPY ./src /home/app/code/src  
COPY ./tests /home/app/code/tests  
  
USER root  
RUN chown -R app /home/app  
  
WORKDIR /home/app/code  
USER app  
RUN make check && make install  
CMD node index.js  


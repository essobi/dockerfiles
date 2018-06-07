FROM node:6.10.3  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
RUN npm install --silent @angular/cli -g  
  
COPY package.json /opt/app/package.json  
  
COPY src /opt/app/src/  
COPY e2e /opt/app/e2e/  
COPY .angular-cli.json /opt/app/.angular-cli.json  
COPY protractor.conf.js /opt/app/protractor.conf.js  
COPY karma.conf.js /opt/app/karma.conf.js  
COPY tslint.json /opt/app/tslint.json  
  
RUN npm install --silent


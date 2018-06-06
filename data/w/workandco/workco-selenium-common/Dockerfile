FROM node:7.8.0  
RUN mkdir /automation/  
  
WORKDIR automation  
  
RUN mkdir -p wdio/config  
  
RUN mkdir -p scripts  
  
RUN mkdir -p specs/unit-tests  
  
COPY package.json /automation  
  
COPY wdio/config/ /automation/wdio/config  
  
COPY scripts/ /automation/scripts  
  
ENV RUN_JEST_TESTS node_modules/jest-cli/bin/jest.js  
  
ENV REPORT_JEST_TESTS /automation/node_modules/custom-jest-json-reporter/  
  
ENV UPLOADJS_TO_S3 /automation/scripts/uploadToS3.js  
  
RUN mkdir -p specs  
  
RUN npm install  


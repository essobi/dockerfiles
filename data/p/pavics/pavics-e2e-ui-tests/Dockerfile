FROM cypress/base  
MAINTAINER Renaud Hébert-Legault <renaud.hebert-legault@crim.ca>  
LABEL Description="PAVICS Platform E2E tests - Based on Node.js and
Cypress.IO" Vendor="CRIM" Version="0.0.1"  
WORKDIR /tests  
  
ENV npm_config_loglevel=warn  
  
ADD package.json package.json  
ADD package-lock.json package-lock.json  
RUN npm install  
ADD . .  
  
# We will split spec.js into multiple videos as soon as its possible  
# Awaiting this PR to be merged in next cypress release
https://github.com/cypress-io/cypress/pull/1583  
CMD ["npm", "test"]


FROM cypress/base  
WORKDIR /tests  
ADD . /tests  
RUN npm install  
RUN $(npm bin)/cypress verify


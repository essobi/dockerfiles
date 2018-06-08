FROM circleci/node:9.11-browsers  
  
USER root  
  
RUN npm i -g lighthouse  
  
ADD . /tmp  
  
CMD ["lighthouse"]  


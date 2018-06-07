FROM node:latest  
  
RUN mkdir /website  
ADD . /website  
WORKDIR /website  
  
RUN npm install  
  
CMD python -m SimpleHTTPServer 8080


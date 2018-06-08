FROM alpine:latest  
  
MAINTAINER lhull@hcpci.com  
  
# Copy app to /src  
COPY . /src  
  
# Install app and dependencies into /src  
RUN apk add --update nodejs  
  
RUN cd /src; npm install  
  
EXPOSE 8080  
CMD cd /src && node ./app.js  
  


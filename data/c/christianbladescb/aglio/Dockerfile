# Pull base image  
FROM alpine:3.3  
LABEL version=2.2.0  
  
RUN apk -U add nodejs g++ make python; npm install -g aglio@2.2.0; apk del g++
make python  
  
ENTRYPOINT ["aglio"]  


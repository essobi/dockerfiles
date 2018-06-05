FROM alpine:3.5  
# inspired by https://github.com/christian-blades-cb/aglio-docker  
RUN apk -U add nodejs g++ make python; npm install -g aglio@2.3.0; apk del g++
make python  
  
ENTRYPOINT ["aglio"]  


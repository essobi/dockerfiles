FROM alpine:latest  
MAINTAINER smccartney  
  
# update alpine linux  
RUN apk update && apk upgrade && \  
apk add nodejs && \  
apk add nodejs-npm && \  
npm install -g @angular/cli@latest  
  
# add source code to images  
ADD . /ncaa-foul-frontend  
  
# switch working directory  
WORKDIR /ncaa-foul-frontend  
  
# install dependencies  
RUN npm install  
  
# expose port 4200  
EXPOSE 4200  
  
# run ng serve on localhost  
CMD ["ng","serve", "--host", "0.0.0.0", "--disable-host-check"]  


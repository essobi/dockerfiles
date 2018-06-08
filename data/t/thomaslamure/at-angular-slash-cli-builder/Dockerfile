FROM docker:latest  
  
RUN apk add --update python build-base nodejs nodejs-npm && npm install
npm@latest -g  
RUN npm install code-point-at  
RUN npm install @angular/cli  
  
CMD echo "Please do not run this image in daemon"  


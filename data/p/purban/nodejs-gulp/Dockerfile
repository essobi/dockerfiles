FROM alpine  
  
RUN apk update &&\  
apk add \--update nodejs  
  
  
ADD script /script  
  
ONBUILD ADD app /app  
ONBUILD WORKDIR /app  
ONBUILD RUN npm install && ./node_modules/gulp/bin/gulp.js  
  
  
ENTRYPOINT [ "/script/bootstrap.sh" ]  
  
CMD [ "start" ]  


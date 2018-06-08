FROM alpine  
  
RUN apk add --update nodejs  
  
ONBUILD ADD app /app  
ONBUILD WORKDIR /app  
ONBUILD RUN npm install  
ONBUILD EXPOSE 8081  
ENTRYPOINT ["/usr/bin/npm"]  


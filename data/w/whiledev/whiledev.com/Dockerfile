FROM alpine:latest  
  
RUN apk add --update --no-cache nodejs  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY index.js /usr/src/app/index.js  
  
EXPOSE 3000  
CMD ["node", "index.js"]  


FROM alpine:3.7  
EXPOSE 8090  
RUN apk add --update --no-cache git  
RUN mkdir -p /app /app/bin/  
  
WORKDIR /app  
  
COPY ./bin/entry /app/bin/  
COPY config.json /app/  
  
CMD ["./bin/entry"]  


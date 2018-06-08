  
FROM golang:1.9.2  
WORKDIR /back/  
  
ADD . /back/  
  
RUN ./install-deps.sh && env GOOS=linux GOARCH=386 go build  
  
FROM alpine:latest  
  
COPY \--from=0 /back/back /bin/  
  
EXPOSE 8080  
CMD [ "back" ]


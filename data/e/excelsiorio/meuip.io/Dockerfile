FROM golang:1.9-alpine  
RUN apk add --no-cache git  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN go get github.com/go-martini/martini && go build -o meuip  
  
FROM alpine:3.6  
COPY \--from=0 /usr/src/app/meuip /usr/local/bin/meuip  
  
EXPOSE 3000  
CMD ["/usr/local/bin/meuip"]


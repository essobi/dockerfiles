FROM golang:1.6-alpine  
MAINTAINER Jetsada Machom <jim@imjim.im>  
  
COPY . /go/src/app  
WORKDIR /go/src/app  
RUN go build  
  
EXPOSE 3000  
CMD ["./app"]  


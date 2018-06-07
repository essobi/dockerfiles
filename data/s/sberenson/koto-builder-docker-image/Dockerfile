FROM golang:1.7.3  
  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
ca-certificates \  
supervisor #  
  
  
  
RUN mkdir -p /checkout  
WORKDIR /checkout  
  
  
RUN go get github.com/constabulary/gb/...  
RUN go get -u github.com/golang/lint/golint  
RUN go get -u github.com/vektra/mockery/...  
  
ENV GOPATH=/checkout/project:/checkout/project/vendor  
  
  
  


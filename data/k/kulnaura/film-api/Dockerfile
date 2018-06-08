FROM golang:1.8.3  
# Create app directory  
RUN mkdir -p /go/src/github.com/lempiy/echo_api  
WORKDIR /go/src/github.com/lempiy/echo_api  
  
# Install code watcher  
RUN go get github.com/pilu/fresh  
  
COPY . /go/src/github.com/lempiy/echo_api  
  
CMD ['fresh']  
  
EXPOSE 8001


FROM golang:1.9.4  
LABEL maintainer Maxime PETIT  
  
# Setup work directory  
WORKDIR /go/src/github.com/mxpetit/candelabot-aggregator  
  
# Install dependencies  
ADD . /go/src/github.com/mxpetit/candelabot-aggregator/  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN dep ensure  
RUN go install -race -v ./...  
  
# Setup environment  
ENV CANDELABOT_ENV=TEST  
  
CMD ["/go/bin/candelabot-aggregator"]  


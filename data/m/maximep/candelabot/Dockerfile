FROM golang:1.9.4  
LABEL maintainer <maximepetit@hotmail.fr>  
  
# Setup work directory  
WORKDIR /go/src/github.com/mxpetit/candelabot  
  
# Install dependencies  
ADD . /go/src/github.com/mxpetit/candelabot/  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN dep ensure  
  
# Setup environment  
ENV CANDELABOT_ENV=TEST  
  
CMD ["go", "run", "candelabot/websocket_example.go"]  


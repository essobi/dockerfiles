FROM golang:1.8-alpine  
RUN apk add --no-cache git curl openssh  
  
WORKDIR "/go"  
  
RUN curl https://glide.sh/get | sh  
RUN go get -u \  
golang.org/x/tools/cmd/godoc \  
cmd/gofmt \  
golang.org/x/tools/cmd/goimports \  
github.com/golang/lint/golint  
  
RUN mkdir /root/.ssh && echo "StrictHostKeyChecking no " > /root/.ssh/config  


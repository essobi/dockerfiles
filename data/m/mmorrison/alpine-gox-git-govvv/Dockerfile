# Gox (go v1.7)  
#  
# docker run --rm -v $GOPATH/src:/go/src -w /go/src/github.com/your-
account/project pottava/gox:1.7 \--osarch "linux/amd64" -output
"dist/{{.OS}}_{{.Arch}}"  
  
FROM golang:1.7-alpine  
  
RUN apk --no-cache add \--virtual build-dependencies git \  
&& go get -u -v github.com/mitchellh/gox \  
&& go get -u -v github.com/ahmetalpbalkan/govvv \  
&& cp /go/bin/* /usr/local/bin/  
  


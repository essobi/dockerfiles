# Gox (go v1.10)  
#  
# docker run --rm -v $GOPATH/src:/go/src -w /go/src/github.com/your-
account/project pottava/gox:go1.10 --osarch "linux/amd64" -output
"dist/{{.OS}}_{{.Arch}}"  
FROM pottava/golang:1.10-builder  
  
RUN apk --no-cache add --virtual build-dependencies git \  
  
# Install gox  
&& go get -u github.com/mitchellh/gox \  
  
# Clean up  
&& apk del --purge -r build-dependencies \  
&& rm -rf /go/src/*  
  
RUN apk --no-cache add gcc musl-dev  
  
ENTRYPOINT ["gox"]  
CMD ["-h"]  


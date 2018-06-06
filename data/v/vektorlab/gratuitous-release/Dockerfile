FROM golang:latest  
  
RUN apt-get -yqq update && apt-get install -yq libmagic-dev  
  
ENV PACKAGE_PATH /go/src/github.com/vektorlab/gratuitous-release  
COPY . "$PACKAGE_PATH"  
  
RUN cd "$PACKAGE_PATH" && \  
go get -u github.com/jteeuwen/go-bindata/... && \  
go-bindata static/ && \  
go get -v -d && \  
go build -ldflags "-s -X main.version=$(git describe)" -o /usr/bin/gratuitous-
release  
  
ENTRYPOINT ["gratuitous-release"]  


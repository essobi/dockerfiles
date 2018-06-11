# Dockerfile for ubuntu wily debian packaging image  
FROM ubuntu:wily  
  
# Install the minimum required packages  
RUN apt-get update -y && apt-get install -y devscripts equivs git golang make
m4  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
RUN go install -v -race runtime/race  


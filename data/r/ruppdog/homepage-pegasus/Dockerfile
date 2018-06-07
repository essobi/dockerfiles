FROM golang:1.6.3-alpine  
  
RUN apk --update add git  
  
# Copy App  
COPY . /go/src/github.com/truppert/homepage-pegasus  
  
# Download Dependencies  
RUN \  
cd /go/src/github.com/truppert/homepage-pegasus && \  
go get  
  
# Build App  
RUN \  
cd /go/src/github.com/truppert/homepage-pegasus && \  
go build  
  
WORKDIR /go/src/github.com/truppert/homepage-pegasus  
  
CMD ["go", "test"]


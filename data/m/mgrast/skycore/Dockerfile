# Skycore factory - a compilation container  
FROM golang:1.6.3-alpine  
  
  
WORKDIR /go/bin  
  
COPY . /go/src/github.com/MG-RAST/Skycore  
  
RUN cd /go/src/github.com/MG-RAST/Skycore && \  
CGO_ENABLED=0 go install -a -installsuffix cgo -v ...  
  
CMD ["/go/bin/skycore"]  


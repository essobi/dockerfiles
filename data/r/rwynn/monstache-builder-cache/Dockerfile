FROM rwynn/monstache-builder:1.0.0  
WORKDIR /go/src/cache-app  
  
COPY monstache-deps-cache.go /go/src/cache-app/monstache-deps-cache.go  
  
RUN go get -d -v ./... && rm -f /go/src/cache-app/monstache-deps-cache.go  


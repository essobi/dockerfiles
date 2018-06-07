FROM golang  
  
MAINTAINER Sandlayth <modepadu95@riseup.net>  
  
RUN apt-get update && apt-get install git make -y  
  
WORKDIR /srv/  
  
RUN go get github.com/GeertJohan/go.rice  
  
RUN go get github.com/GeertJohan/go.rice/rice  
  
RUN go get github.com/Depado/goploader/server  
  
RUN rice embed-go -i=github.com/Depado/goploader/server  
  
RUN go build -o server github.com/Depado/goploader/server  
  
CMD ["./server","--initial"]  
  


FROM golang:1.6.2  
  
RUN apt-get update  
RUN apt-get upgrade -y --force-yes  
RUN apt-get install -y --force-yes curl libmagic-dev gcc apt-transport-https  
  
ENV GOROOT /usr/local/go  
RUN go get -v -u "github.com/HolmesProcessing/Holmes-Storage"  
RUN mkdir -p /data/holmes-storage/  
WORKDIR /data/holmes-storage/  
  
CMD ["/go/bin/Holmes-Storage", "--config=config.json"]  


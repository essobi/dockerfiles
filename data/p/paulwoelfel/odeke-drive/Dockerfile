FROM golang:latest  
MAINTAINER Paul Woelfel <github@frig.at>  
  
RUN go get -u github.com/odeke-em/drive/cmd/drive \  
&& mkdir /drive  
  
WORKDIR /drive  
ENTRYPOINT ["/go/bin/drive"]  
CMD []  


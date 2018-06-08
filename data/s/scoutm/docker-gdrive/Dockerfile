FROM golang:1.6  
ENV GOPATH /usr/src/go  
ENV PATH $PATH:$GOPATH/bin  
  
RUN apt-get update && \  
apt-get install pigz buffer -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN go get github.com/prasmussen/gdrive && \  
go install github.com/prasmussen/gdrive  
  
WORKDIR /  
  
CMD ["/bin/bash"]  


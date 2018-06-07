FROM ubuntu:latest  
RUN apt-get update  
RUN apt-get install -y golang git mercurial  
ENV GOPATH $HOME/gopath  
RUN go get -u github.com/odeke-em/drive/cmd/drive  
ADD download.sh /download.sh  
CMD ["/download.sh"]  


FROM google/golang  
MAINTAINER Sevki <s@sevki.org>  
  
ADD . /gopath/src/willnorris.com/go/imageproxy  
RUN go get willnorris.com/go/imageproxy/cmd/imageproxy  
  
CMD []  
ENTRYPOINT ["/gopath/src/willnorris.com/go/imageproxy/scripts/run.sh"]  
  
EXPOSE 8080  


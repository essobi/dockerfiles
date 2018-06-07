FROM golang  
MAINTAINER Jake Robinson <jaker@vmware.com>  
  
ENV GOPATH=/root/  
  
RUN go get -u github.com/vmware/vic/cmd/vcsim  
  
EXPOSE 8989  
CMD /root/bin/vcsim -httptest.serve 0.0.0.0:8989  


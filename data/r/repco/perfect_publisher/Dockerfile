#####################  
# perfect_publisher #  
#####################  
  
FROM repco/perfect_common:latest  
  
MAINTAINER Colin Hom  
  
ADD . /root/gopath/src/github.com/repco/perfect_publisher  
  
RUN go get -v github.com/repco/perfect_publisher  
  
ENTRYPOINT ["/root/gopath/bin/perfect_publisher"]


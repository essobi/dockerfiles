#######################  
# perfect_api #  
#######################  
  
# Set the base image to Ubuntu  
FROM repco/perfect_common:latest  
  
# File Author / Maintainer  
MAINTAINER Colin Hom  
  
ADD . /root/gopath/src/github.com/repco/perfect_api  
RUN go get -v ./src/github.com/repco/perfect_api  
  
EXPOSE 1618  
  
ENTRYPOINT ["/root/gopath/bin/perfect_api"]  


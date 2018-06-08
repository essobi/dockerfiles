# An image that can be used to build a golang source repository  
# Requires you to set the GOREPO env variable to a value that can be  
# passed to `go get`  
# Executables are copied to /usr/local/bin  
FROM pallet/golang  
MAINTAINER hugo@palletops.com  
  
RUN apt-get -y install git  
ADD build-go-get build-go-get  
ONBUILD ADD gorepo gorepo  
ONBUILD RUN ["/bin/bash", "build-go-get"]  
ONBUILD RUN cp $GOPATH/bin/* /usr/local/bin  
ONBUILD RUN rm -rf $GOPATH  
ONBUILD RUN apt-get -y remove go golang-go git  
ONBUILD RUN apt-get -y autoremove  
ONBUILD RUN apt-get -y autoclean  
ONBUILD RUN apt-get -y clean  


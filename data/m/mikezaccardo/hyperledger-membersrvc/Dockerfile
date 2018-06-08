# Dockerfile for Hyperledger membersrvc image. This actually follow
hyperledger  
# image but to make sure the config is done.  
# Data is stored under /var/hyperledger/db and /var/hyperledger/production  
FROM mikezaccardo/hyperledger:latest  
MAINTAINER Baohua Yang  
  
RUN cd $GOPATH/src/github.com/hyperledger/fabric/membersrvc \  
&& CGO_CFLAGS=" " CGO_LDFLAGS="-lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy" go
install \  
&& cp membersrvc.yaml $GOPATH/bin \  
&& go clean  
  
CMD ["membersrvc"]  


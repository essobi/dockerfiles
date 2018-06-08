FROM google/golang  
  
WORKDIR /gopath/src/app  
ADD . /gopath/src/app/  
RUN go get app  
RUN go install  
  
CMD /gopath/bin/app -topic=$TOPIC -lookup-address=$LOOKUPD_ADDR -output-tcp-
address=$OUTPUT_TCP_ADDR  


FROM google/golang:1.3  
RUN go get github.com/mitchellh/gox  
RUN gox -build-toolchain  
  
ADD ./gox-docker /usr/bin/gox-docker  
ENTRYPOINT ["gox-docker"]  


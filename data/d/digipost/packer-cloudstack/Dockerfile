FROM golang  
MAINTAINER larstobi@relatime.no  
  
RUN go get github.com/mitchellh/gox  
RUN go get github.com/mitchellh/packer  
  
# packer-cloudstack only builds with Packer 0.7.5  
WORKDIR /go/src/github.com/mitchellh/packer  
RUN git checkout -b v0.7.5 v0.7.5 && go clean  
  
# Packer 0.7.5 does not build from source anymore, so get the binaries.  
WORKDIR /go/bin  
RUN apt-get update && apt-get install -y bsdtar && apt-get clean  
RUN curl -s -L
https://dl.bintray.com/mitchellh/packer/packer_0.7.5_linux_amd64.zip | bsdtar
--no-same-owner --no-same-permissions -xf-  
RUN chmod 0555 packer*  
  
# Build and install packer-cloudstack  
RUN go get github.com/schubergphilis/packer-cloudstack  
RUN make -C $GOPATH/src/github.com/schubergphilis/packer-cloudstack dev  
  
RUN useradd -d /packer packer  
USER packer  
VOLUME /packer  
WORKDIR /packer  
ENTRYPOINT ["/go/bin/packer"]  


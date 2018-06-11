FROM golang:latest  
MAINTAINER stefan wuthrich <info@exponity.ch>  
  
EXPOSE 5000  
RUN \  
curl -sSL https://nodejs.org/dist/v5.3.0/node-v5.3.0-linux-x64.tar.gz |\  
tar -xzf - --strip-components=1 -C /usr/local  
  
WORKDIR /go/  
  
ADD . src/bitbucket.org/horisen/verifycenterweb  
RUN cd src/bitbucket.org/horisen/verifycenterweb && npm install  
RUN go get github.com/jteeuwen/go-bindata/... # && go get
bitbucket.org/horisen/verifycenterweb/server  
#CMD go install bitbucket.org/horisen/verifycenterweb/server  
WORKDIR "/go/src/bitbucket.org/horisen/verifycenterweb"  
#ENTRYPOINT /go/bin/verifycenterweb  
RUN . /go/src/bitbucket.org/horisen/verifycenterweb/start.sh  
CMD ["/go/bin/verifycenterweb", "run"]


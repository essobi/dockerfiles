# Using wheezy from the official golang docker repo  
FROM golang:1.6.3-wheezy  
  
# Setting up working directory  
ADD . $GOPATH/src/bitbucket.org/goboot/geoseva  
WORKDIR $GOPATH/src/bitbucket.org/goboot/geoseva  
  
# Get godeps from main repo  
RUN go get github.com/tools/godep  
  
# Restore godep dependencies  
RUN godep restore  
  
# Install  
RUN go install bitbucket.org/goboot/geoseva  
  
# Setting up environment variables  
ENV ENV dev  
  
# My web app is running on port 3000 so exposed that port for the world  
EXPOSE 3000  
ENTRYPOINT ["/go/bin/geoseva"]  


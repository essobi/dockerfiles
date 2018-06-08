FROM golang:1.8-alpine  
  
# gox - Go cross compile tool  
# github-release - Github Release and upload artifacts  
# go-junit-report - convert Go test into junit.xml format  
RUN apk add --no-cache git && \  
go get -v github.com/mitchellh/gox && \  
go get -v github.com/aktau/github-release && \  
go get -v github.com/jstemmer/go-junit-report  
  
# Create and set working directory
'/go/src/github.com/${GH_USER}/${GH_PROJECT}'  
ONBUILD RUN if [ -z "$GH_USER" ]; then echo "Build with '--build-arg GH_USER'"
&& exit -1; fi  
ONBUILD RUN if [ -z "$GH_PROJECT" ]; then echo "Build with '--build-arg
GH_PROJECT'" && exit -1; fi  
ONBUILD RUN mkdir -p /go/src/github.com/${GH_USER}/${GH_PROJECT}  
# set working directory  
ONBUILD WORKDIR /go/src/github.com/${GH_USER}/${GH_PROJECT}  
  
# copy sources  
ONBUILD COPY . .  
  
# default CMD build script  
ONBUILD CMD ["script/go_build.sh"]  
  


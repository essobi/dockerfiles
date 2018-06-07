##########################################################  
# Dockerfile which builds a simple Go restservicce  
##########################################################  
FROM golang  
  
ADD . /go/src/fag-ark-reaktiv-isolat  
  
RUN go get github.com/goarne/web  
RUN go get github.com/goarne/logging  
  
RUN go install fag-ark-reaktiv-isolat && \  
mkdir /config && \  
mkdir /logs && \  
cp /go/src/fag-ark-reaktiv-isolat/config/appconfig.json
/config/appconfig_docker.json  
  
  
  
  
EXPOSE 9998  
  
WORKDIR /  
  
CMD $GOPATH/bin/fag-ark-reaktiv-isolat -config=/config/appconfig_docker.json  
  


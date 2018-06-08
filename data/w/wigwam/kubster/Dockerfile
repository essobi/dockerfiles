# Build app stage  
FROM golang AS build-env  
ADD . /go/src/kubster  
RUN cd /go/src/kubster && go get -v -d .  
RUN cd /go/src/kubster && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix
cgo -o kubster .  
  
# Build image stage  
FROM scratch  
COPY \--from=build-env /go/src/kubster/kubster /  
ENTRYPOINT ["/kubster"]  


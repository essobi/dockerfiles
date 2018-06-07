FROM golang  
MAINTAINER Frederic Branczyk <fbranczyk@gmail.com>  
  
RUN go get github.com/tools/godep  
  
RUN mkdir -p /go/src/github.com/emerald-ci/test-runner  
COPY . /go/src/github.com/emerald-ci/test-runner  
RUN cd /go/src/github.com/emerald-ci/test-runner && make linux  
RUN mv /go/src/github.com/emerald-ci/test-runner/bundles/test-runner_linux-
amd64 /bin/test-runner && chmod +x /bin/test-runner  
  
WORKDIR /project  
ENTRYPOINT ["/bin/test-runner"]  
  


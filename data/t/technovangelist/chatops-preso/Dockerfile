FROM golang  
MAINTAINER Matt Williams  
  
# RUN go get github.com/go-martini/martini  
# RUN go get github.com/paulbellamy/ratecounter  
# RUN go get github.com/garyburd/redigo/redis  
# RUN go get github.com/mitchellh/goamz/aws  
# RUN go get github.com/mitchellh/goamz/s3  
RUN go get -u bitbucket.org/ddevangelist/dddemo  
# RUN go install -i dd-demo  
WORKDIR /go/src/bitbucket.org/ddevangelist/dddemo  
ENTRYPOINT /go/bin/dddemo  
EXPOSE 8000  


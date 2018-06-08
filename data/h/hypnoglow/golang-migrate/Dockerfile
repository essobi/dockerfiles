FROM golang:1.10-alpine3.7 AS build  
  
ENV VERSION v3.2.0  
RUN apk add --no-cache git  
  
RUN go get -v -d github.com/golang-migrate/migrate/cli \  
&& go get -v -d github.com/lib/pq  
  
WORKDIR /go/src/github.com/golang-migrate/migrate  
  
RUN git checkout ${VERSION} \  
&& go build -tags 'postgres' -o ./bin/migrate ./cli  
  
FROM alpine:3.7  
COPY \--from=build /go/src/github.com/golang-migrate/migrate/bin/migrate
/usr/local/bin/migrate  
  
ENTRYPOINT ["migrate"]  


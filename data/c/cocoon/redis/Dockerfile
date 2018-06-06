FROM golang:1.8.3 as builder  
#WORKDIR /go/src/bitbucket.org/cocoon_bitbucket/redis  
# get redis exporter dependencies  
RUN go get -d -v github.com/garyburd/redigo/redis && \  
go get -d -v github.com/prometheus/client_golang/prometheus && \  
go get -d -v github.com/prometheus/client_golang/prometheus/promhttp  
#go get -d -v github.com/cloudfoundry-community/go-cfenv  
# get cocoon redis exporter ( this repo)  
RUN go get -d -v bitbucket.org/cocoon_bitbucket/redis  
  
# build redis_exporter  
WORKDIR /go/src/bitbucket.org/cocoon_bitbucket/redis  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o redis_exporter
.  
  
#FROM alpine:latest  
FROM redis:alpine  
  
RUN apk --no-cache add ca-certificates  
  
COPY redis.conf /usr/local/etc/redis.conf  
COPY docker-entrypoint.sh /usr/local/bin/  
  
#COPY files/etc_sysctl.d_10-redis.conf /etc/sysctl.d/10-redis.conf  
#RUN sysctl vm.overcommit_memory=1  
WORKDIR /app/  
RUN chmod +w /app  
COPY \--from=builder
go/src/bitbucket.org/cocoon_bitbucket/redis/redis_exporter .  
#CMD ["./redis_exporter"]


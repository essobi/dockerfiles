FROM golang:alpine as builder  
  
#Snapshots 2018-01-10-23:14:45  
ENV HORIZON_VERSION=eb8599c75aebcbe2fbf89fba3a5d9e13a4402201  
  
# deploy bifrost binary  
ADD initial_balance_fix.patch /  
ADD healthcheck.patch /  
RUN mkdir -p /go/src/github.com/stellar/ \  
&& apk add --no-cache git wget glide mercurial gcc musl-dev ca-certificates \  
&& git clone https://github.com/stellar/go.git /go/src/github.com/stellar/go \  
&& cd /go/src/github.com/stellar/go \  
&& git checkout $HORIZON_VERSION \  
&& git apply /initial_balance_fix.patch \  
&& git apply /healthcheck.patch \  
&& glide install \  
&& go install github.com/stellar/go/services/bifrost  
  
# deploy config manager  
RUN wget -nv -O /usr/local/bin/confd \  
https://github.com/kelseyhightower/confd/releases/download/v0.14.0/confd-0.14.0-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd  
  
# deploy db init script  
ADD initbifrost /go/src/github.com/stellar/initbifrost  
RUN go get github.com/lib/pq \  
&& go install github.com/stellar/initbifrost  
  
FROM alpine:latest  
  
ADD confd /etc/confd  
COPY \--from=builder /go/bin/bifrost /go/bin/bifrost  
COPY \--from=builder /go/bin/initbifrost /go/bin/initbifrost  
COPY \--from=builder
/go/src/github.com/stellar/go/services/bifrost/database/migrations/01_init.sql
/go/src/github.com/stellar/go/services/bifrost/database/migrations/01_init.sql  
COPY \--from=builder /usr/local/bin/confd /usr/local/bin/confd  
  
ADD entry.sh /entry.sh  
RUN chmod +x /entry.sh  
ENTRYPOINT ["/entry.sh"]  
  
EXPOSE 8000  


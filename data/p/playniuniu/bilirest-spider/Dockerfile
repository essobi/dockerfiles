FROM golang:alpine as builder  
  
COPY src/ /opt/src  
COPY Makefile /opt  
  
WORKDIR /opt  
  
RUN apk add --update make upx git  
RUN go get -u github.com/sirupsen/logrus \  
&& go get -u github.com/fatih/color \  
&& go get -u github.com/spf13/cobra\  
&& go get -u github.com/jinzhu/gorm \  
&& go get -u github.com/lib/pq  
RUN make docker  
  
FROM alpine  
  
COPY \--from=builder /opt/tspider /usr/local/bin/  
COPY run.sh .  
RUN apk add --no-cache --update postgresql-client ca-certificates  
  
CMD [ "./run.sh" ]


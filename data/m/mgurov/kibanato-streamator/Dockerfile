FROM golang:1.9.2 as builder  
RUN go get -u github.com/kardianos/govendor  
WORKDIR /go/src/github.com/mgurov/streamator  
ADD vendor/vendor.json ./vendor/vendor.json  
RUN govendor sync  
RUN sed -i 's|Sirupsen/logrus|sirupsen/logrus|g'
./vendor/gopkg.in/sohlich/elogrus.v1/hook.go #A hackish workaround to
inconsistency of this dependency spelling our dependnecies  
ADD *.go ./  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /usr/bin/app .  
  
FROM scratch  
COPY \--from=builder /usr/bin/app .  
ENTRYPOINT ["./app"]


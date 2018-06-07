FROM golang:1.9  
RUN go get -u github.com/kardianos/govendor  
  
WORKDIR /go/src/github.com/discordianfish/pubgtracker_exporter  
  
COPY vendor/ vendor/  
RUN govendor sync  
  
COPY . .  
RUN CGO_ENABLED=0 go build .  
RUN ls  
  
FROM alpine:3.6  
RUN apk add --update ca-certificates && adduser -D user  
USER user  
COPY \--from=0
/go/src/github.com/discordianfish/pubgtracker_exporter/pubgtracker_exporter /  
  
EXPOSE 8080  
ENTRYPOINT [ "/pubgtracker_exporter" ]  


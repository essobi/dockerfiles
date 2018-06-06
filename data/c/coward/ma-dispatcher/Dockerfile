FROM golang as builder  
  
WORKDIR /go/src/github.com/dgmann/ma-dispatcher  
COPY . .  
  
RUN go-wrapper download && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix
cgo -o /dispatcher .  
  
FROM scratch  
ADD ca-certificates.crt /etc/ssl/certs/  
COPY \--from=builder /dispatcher /dispatcher  
  
EXPOSE 80  
CMD ["/dispatcher"]


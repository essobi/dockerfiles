FROM golang as builder  
WORKDIR /go/src/github.com/dgmann/ma-output  
COPY . .  
RUN go-wrapper download && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix
cgo -o /output .  
  
FROM scratch  
COPY \--from=builder /output /output  
VOLUME /stats  
CMD ["/output"]


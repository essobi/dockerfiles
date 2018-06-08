FROM alpine:3.6 as builder  
RUN apk --no-cache add go libc-dev git govendor  
RUN mkdir -p /go/src/github.com/kochman/repostatus/vendor  
ENV GOPATH=/go  
WORKDIR $GOPATH/src/github.com/kochman/repostatus  
COPY vendor/vendor.json vendor/vendor.json  
RUN govendor sync  
RUN govendor install +vendor +std  
COPY . .  
RUN go build -o repostatus  
  
FROM alpine:3.6  
RUN apk --no-cache add ca-certificates  
RUN mkdir -p /app/static  
WORKDIR /app  
COPY \--from=builder /go/src/github.com/kochman/repostatus/repostatus
/go/src/github.com/kochman/repostatus/status.html /app/  
COPY \--from=builder /go/src/github.com/kochman/repostatus/static/
/app/static/  
EXPOSE 5000  
CMD ["/app/repostatus"]  


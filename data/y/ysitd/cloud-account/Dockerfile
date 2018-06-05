FROM ysitd/dep AS builder  
  
WORKDIR /go/src/code.ysitd.cloud/component/account  
  
COPY . /go/src/code.ysitd.cloud/component/account  
  
RUN dep ensure -vendor-only && \  
go build -o account ./cmd/server.go  
  
FROM alpine:3.6  
  
COPY --from=builder /go/src/code.ysitd.cloud/component/account/account /  
  
CMD ["/account"]


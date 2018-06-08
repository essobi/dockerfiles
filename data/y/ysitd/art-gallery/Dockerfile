FROM ysitd/dep AS builder  
  
WORKDIR /go/src/code.ysitd.cloud/component/art/gallery  
  
COPY . /go/src/code.ysitd.cloud/component/art/gallery  
  
RUN dep ensure -vendor-only && \  
go build -v  
  
FROM alpine:3.6  
RUN apk add --no-cache ca-certificates  
  
COPY \--from=builder /go/src/code.ysitd.cloud/component/art/gallery/gallery /  
  
CMD ["/gallery"]  


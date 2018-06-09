FROM ysitd/glide as builder  
  
ADD . /go/src/code.ysitd.cloud/component/status  
  
WORKDIR /go/src/code.ysitd.cloud/component/status  
  
RUN glide install -v && \  
go build -v -ldflags "-s -w"  
  
FROM alpine:3.6  
COPY \--from=builder /go/src/code.ysitd.cloud/component/status/status /  
  
ENV PORT 80  
EXPOSE 80  
CMD ["/status"]  


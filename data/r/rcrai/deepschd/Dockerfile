FROM registry.cn-zhangjiakou.aliyuncs.com/yuikns/go-deps as builder  
#FROM yuikns/go-deps as builder  
ADD . /go/src/github.com/rcrai/deepschd  
  
RUN cd /go/src/github.com/rcrai/deepschd && bash ./build.sh  
  
FROM scratch  
  
# x509: failed to load system roots and no roots provided  
COPY \--from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
  
#COPY --from=builder /go/bin/sunlab-api /sunlab-api  
COPY \--from=builder /go/src/github.com/rcrai/deepschd/deepschd /deepschd  
  
EXPOSE 10023  
EXPOSE 10123  
ENTRYPOINT ["/deepschd"]  
  


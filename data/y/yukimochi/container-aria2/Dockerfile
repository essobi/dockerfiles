FROM alpine:latest AS builder  
  
RUN apk add -U --no-cache aria2 ca-certificates  
WORKDIR /tmp/rootfs  
RUN mkdir -p etc/ssl/certs usr/bin usr/lib lib && \  
cp /usr/bin/aria2c usr/bin && \  
cp /etc/ssl/certs/ca-certificates.crt etc/ssl/certs && \  
for lib in $(ldd usr/bin/aria2c | awk '{ print $(NF-1) }'); do \  
cp $lib .$lib; \  
done  
  
FROM scratch  
  
COPY \--from=builder /tmp/rootfs /  
WORKDIR /data  
VOLUME [ "/data" ]  
EXPOSE 6800  
ENTRYPOINT [ "aria2c" ]  
CMD [ "--enable-rpc", "--rpc-listen-all" ]  


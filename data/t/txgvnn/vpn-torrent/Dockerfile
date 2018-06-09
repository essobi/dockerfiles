FROM golang:1.7.3 as builder  
WORKDIR /autovpn  
RUN git clone \--depth 1 https://github.com/adtac/autovpn /autovpn && \  
sed -i s/\"sudo\",//g autovpn.go && \  
CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .  
  
FROM alpine:latest  
RUN apk --no-cache add openvpn rtorrent screen  
COPY \--from=builder /autovpn/app .  
ADD entrypoint.sh /  
WORKDIR /data  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["sh"]  


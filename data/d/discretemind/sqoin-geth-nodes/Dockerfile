FROM golang:1.9-alpine as builder  
  
RUN cd /  
RUN apk add --update git go make gcc curl musl-dev linux-headers  
  
RUN git clone -b release/1.7 https://github.com/ethereum/go-ethereum  
  
RUN ls .  
  
RUN cd go-ethereum && make geth  
  
RUN ls go-ethereum/build/bin/geth  
  
FROM alpine:latest  
  
RUN apk add --no-cache ca-certificates  
COPY \--from=builder /go/go-ethereum/build/bin/geth /usr/local/bin/  
RUN ls /usr/local/bin/  
  
ADD start.sh /root/start.sh  
ADD password /root/password  
ADD onwork.js /root/onwork.js  
  
COPY ./genesis.json /root/genesis.json  
COPY UTC--2017-10-06T08-33-28.676059264Z--
9e286e5ee811c44133ee8acf72ccaf9f953de260 /root/UTC--
2017-10-06T08-33-28.676059264Z--9e286e5ee811c44133ee8acf72ccaf9f953de260  
  
RUN chmod +x /root/start.sh  
RUN chmod +x /root/onwork.js  
WORKDIR /root  
  
ENV GETH_ID=  
ENV GETH_PORT=  
ENV GETH_NETWORK=  
ENV GETH_RPCPORT=  
ENV GETH_ENODE=  
  
EXPOSE 8545  
EXPOSE 30303  
ENTRYPOINT ["/root/start.sh"]  


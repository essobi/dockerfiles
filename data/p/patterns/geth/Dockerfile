FROM alpine  
  
MAINTAINER 興怡  
ENV PROJ_DIR /go/src/go-ethereum  
RUN addgroup alpine \  
&& adduser -G alpine -s /bin/sh -D alpine \  
&& echo "alpine:alpine" | /usr/sbin/chpasswd \  
&& apk --no-cache add git go make gcc musl-dev linux-headers \  
&& git clone https://github.com/ethereum/go-ethereum $PROJ_DIR \  
&& (cd $PROJ_DIR && make) \  
&& cp $PROJ_DIR/build/bin/geth /usr/local/bin/ \  
&& apk del git go make gcc musl-dev linux-headers \  
&& rm -rf /apk /tmp/* /var/cache/apk/* $PROJ_DIR  
  
WORKDIR /home/alpine  
USER alpine  
EXPOSE 8545  
EXPOSE 30303  
EXPOSE 30303/udp  
ENTRYPOINT ["geth"]  
  


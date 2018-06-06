FROM alpine:latest  
  
ENV REFRESHED_AT 2017-07-26  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 27327  
ENV PASSWORD misaki  
ENV METHOD aes-256-ctr  
ENV PROTOCOL auth_chain_a  
ENV PROTOCOLPARAM 32  
ENV OBFS tls1.2_ticket_auth_compatible  
ENV TIMEOUT 300  
ENV DNS_ADDR 8.8.8.8  
ENV DNS_ADDR_2 8.8.4.4  
ENV TZ 'Asia/Shanghai'  
ENV KCP_VERSION 20170525  
ENV KCP_SERVER_PORT 27372  
ENV WORK_HOST 127.0.0.1  
ENV MODE fast2  
  
ARG BRANCH=manyuser  
ARG HOME=~  
  
  
RUN apk --no-cache add python \  
libsodium \  
wget \  
bash  
  
RUN mkdir -p $HOME && \  
wget -qO- --no-check-certificate
https://github.com/shadowsocksr/shadowsocksr/archive/$BRANCH.tar.gz | tar -xzf
- -C $HOME  
  
RUN mkdir -p $HOME \  
&& wget -qO- --no-check-certificate
https://github.com/xtaci/kcptun/releases/download/v$KCP_VERSION/kcptun-linux-
amd64-$KCP_VERSION.tar.gz \  
| tar -zxf - -C $HOME \  
&& mv $HOME/server_linux_amd64 /usr/bin/kcptun \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& rm -rf $HOME/client_linux_amd64 \  
/var/cache/apk/*  
  
RUN echo "python server.py -p $SERVER_PORT -k $PASSWORD -m $METHOD -O
$PROTOCOL -o $OBFS -G $PROTOCOLPARAM >> /$HOME/ssr_kcp.log 2>&1 &" >
/usr/bin/ssr_kcp.sh \  
&& echo "kcptun -t $WORK_HOST:$SERVER_PORT -l :$KCP_SERVER_PORT -mode $MODE >>
/$HOME/ssr_kcp.log 2>&1 &" >> /usr/bin/ssr_kcp.sh \  
&& echo "tail -f /$HOME/ssr_kcp.log" >> /usr/bin/ssr_kcp.sh \  
&& echo "Valar Morghulis" >> /$HOME/ssr_kcp.log \  
&& chmod +x /usr/bin/ssr_kcp.sh  
  
WORKDIR $HOME/shadowsocksr-$BRANCH/shadowsocks  
  
EXPOSE $SERVER_PORT/tcp  
EXPOSE $KCP_SERVER_PORT/udp  
  
CMD ssr_kcp.sh  


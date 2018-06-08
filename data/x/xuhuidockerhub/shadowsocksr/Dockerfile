FROM alpine:3.6  
MAINTAINER Xuhui <1498472791@qq.com> ref:breakwa11/shadowsocksr  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 51348  
ENV PASSWORD psw  
ENV METHOD chacha20  
ENV PROTOCOL auth_aes128_md5  
ENV PROTOCOLPARAM 32  
ENV OBFS tls1.2_ticket_auth_compatible  
ENV TIMEOUT 300  
ENV DNS_ADDR 8.8.8.8  
ENV DNS_ADDR_2 8.8.4.4  
ARG BRANCH=manyuser  
ARG WORK=~  
  
  
RUN apk --no-cache add python \  
build-base \  
gcc \  
openssl-dev \  
musl-dev \  
libsodium \  
wget \  
py2-pip \  
tzdata \  
python-dev \  
libevent-dev \  
py-setuptools \  
py2-gevent \  
\--repository http://mirrors.ustc.edu.cn/alpine/v3.4/main/ --allow-untrusted
&& \  
pip install \  
M2Crypto  
  
RUN mkdir -p $WORK && \  
wget -qO- --no-check-certificate https://github.com/shadowsocksr-
backup/shadowsocksr/archive/$BRANCH.tar.gz | tar -xzf - -C $WORK && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
WORKDIR $WORK/shadowsocksr-$BRANCH/shadowsocks  
  
RUN apk del \  
wget \  
tzdata && \  
rm -rf /tmp/* && rm -rf /var/cache/apk/* && rm -rf /var/lib/apk/*  
  
EXPOSE $SERVER_PORT  
  
CMD python server.py -p $SERVER_PORT -k $PASSWORD -m $METHOD -O $PROTOCOL -o
$OBFS -G $PROTOCOLPARAM  


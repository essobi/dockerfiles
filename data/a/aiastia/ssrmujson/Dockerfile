FROM alpine:edge  
  
  
ARG BRANCH=abcd  
ARG WORK=tmp  
ARG URL1=https://raw.githubusercontent.com/aiastia/mudbjsonss/master/mudb.json  
ARG
URL2=https://raw.githubusercontent.com/aiastia/mudbjsonss/master/userapiconfig.py  
  
RUN apk --no-cache add python \  
libsodium \  
git \  
wget && \  
  
cd /tmp/ && \  
git clone -b abcd https://github.com/shadowsocksR-private/shadowsocksR.git &&
\  
cd shadowsocksR && \  
chmod +x *.sh && \  
chmod +x shadowsocks/*.sh && \  
cp mysql.json usermysql.json && \  
wget -qO 1.json --no-check-certificate $URL1 && \  
cp 1.json mudb.json && \  
wget -qO 2.py --no-check-certificate $URL2 && \  
cp 2.py userapiconfig.py && \  
cd /tmp/ && \  
cd shadowsocksR && \  
rm -rf 1.json && \  
rm -rf 2.py  
  
  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 51348  
ENV PASSWORD psw  
ENV METHOD aes-128-ctr  
ENV PROTOCOL auth_aes128_md5  
ENV PROTOCOLPARAM 32  
ENV OBFS tls1.2_ticket_auth_compatible  
ENV TIMEOUT 300  
ENV DNS_ADDR 8.8.8.8  
ENV DNS_ADDR_2 8.8.4.4  
WORKDIR /$WORK/shadowsocksR  
  
CMD ["python server.py"]  
  


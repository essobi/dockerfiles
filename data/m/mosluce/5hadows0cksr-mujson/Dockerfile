FROM alpine:3.6  
#ENV SERVER_ADDR 0.0.0.0  
#ENV SERVER_PORT 51348  
#ENV PASSWORD psw  
#ENV METHOD aes-128-ctr  
#ENV PROTOCOL auth_aes128_md5  
#ENV PROTOCOLPARAM 32  
#ENV OBFS tls1.2_ticket_auth_compatible  
#ENV TIMEOUT 300  
#ENV DNS_ADDR 8.8.8.8  
#ENV DNS_ADDR_2 8.8.4.4  
ARG BRANCH=manyuser  
ARG WORK=~  
  
  
RUN apk --no-cache add python \  
libsodium \  
wget \  
bash  
  
RUN mkdir -p $WORK && \  
wget -qO- --no-check-certificate https://github.com/shadowsocksr-
backup/shadowsocksr/archive/$BRANCH.tar.gz | tar -xzf - -C $WORK  
  
#WORKDIR $WORK/shadowsocksr-$BRANCH/shadowsocks  
WORKDIR $WORK/shadowsocksr-$BRANCH  
  
#EXPOSE $SERVER_PORT  
#CMD python server.py -p $SERVER_PORT -k $PASSWORD -m $METHOD -O $PROTOCOL -o
$OBFS -G $PROTOCOLPARAM  
#RUN bash initcfg.sh  
RUN chmod +x *.sh  
RUN chmod +x shadowsocks/*.sh  
RUN cp apiconfig.py userapiconfig.py  
RUN cp config.json user-config.json  
RUN cp mysql.json usermysql.json  
  
RUN sed -i "s/API_INTERFACE = 'sspanelv2'/API_INTERFACE = 'mudbjson'/"
userapiconfig.py  
RUN sed -i "s/SERVER_PUB_ADDR = '127.0.0.1'/SERVER_PUB_ADDR = '$(wget -qO- -t1
-T2 ipinfo.io/ip)'/" userapiconfig.py  
  
CMD /usr/bin/python server.py  


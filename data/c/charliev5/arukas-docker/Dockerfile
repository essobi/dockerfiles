FROM alpine:edge  
MAINTAINER Charlie Wang <272876047@qq.com>  
  
RUN apk add --update build-base openssh sudo \  
libev libnet-dev libpcap-dev libressl2.5-libcrypto libsodium musl pcre udns
git\  
&& rm -rf /tmp/* /var/cache/apk/*  
  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
rm -r /root/.cache  
  
RUN echo "root:password"|chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN git clone -b manyuser https://github.com/shadowsocksr/shadowsocksr.git ssr  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh  
  
RUN mv net_speeder /usr/sbin  
COPY entrypoint.sh /usr/sbin  
RUN chmod +x /usr/sbin/entrypoint.sh  
RUN chmod +x /usr/sbin/net_speeder  
  
# Configure container to run as an executable  
ENTRYPOINT ["/usr/sbin/entrypoint.sh"]  


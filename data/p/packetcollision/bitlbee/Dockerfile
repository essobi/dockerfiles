FROM debian:jessie  
MAINTAINER Daniel Nelson <daniel@dcn.io>  
  
RUN apt-get update && \  
apt-get install -y git build-essential gnutls-dev ca-certificates
libgcrypt11-dev \  
libglib2.0-dev xmlto xsltproc asciidoc &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN useradd -d /var/lib/bitlbee \--no-create-home \--shell /usr/sbin/nologin
bitlbee  
RUN mkdir -p /var/lib/bitlbee/ /var/run/bitlbee  
RUN chown -R bitlbee /var/lib/bitlbee/ /run  
  
EXPOSE 6667  
  
ENV BITLBEE_VERSION 3.2.2-1-hip-cat  
  
RUN git clone -b feat/hip-cat https://github.com/bitlbee/bitlbee.git  
  
WORKDIR /bitlbee  
RUN ./configure --prefix=/usr --etcdir=/etc/bitlbee  
RUN make && \  
(cd doc && make -C user-guide)  
RUN make install && \  
make install-etc && \  
echo "Welcome to BitlBee $BITLBEE_VERSION" > /etc/bitlbee/motd.txt  
  
USER bitlbee  
VOLUME /var/lib/bitlbee  
  
ENTRYPOINT ["bitlbee", "-nDv"]  


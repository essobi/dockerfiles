FROM debian:jessie  
  
ENV NETDATA_PORT 19999  
  
RUN apt-get update && \  
apt-get -y install zlib1g-dev uuid-dev libmnl-dev gcc make git \  
autoconf autoconf-archive autogen automake pkg-config \  
curl jq nodejs && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone https://github.com/firehol/netdata.git /netdata.git --depth=1 &&
\  
cd /netdata.git/ && ./netdata-installer.sh \--dont-wait --dont-start-it && \  
cd / && rm -rf /netdata.git  
  
RUN ln -sf /dev/stdout /var/log/netdata/access.log && \  
ln -sf /dev/stdout /var/log/netdata/debug.log && \  
ln -sf /dev/stderr /var/log/netdata/error.log  
  
EXPOSE $NETDATA_PORT  
  
CMD /usr/sbin/netdata -nd -ch /host -p ${NETDATA_PORT}  


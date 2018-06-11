FROM debian:jessie  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y build-essential curl libssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl https://www.unrealircd.org/downloads/Unreal3.2.10.4.tar.gz | tar xz
&& \  
cd Unreal3.2.10.4 && \  
./configure \  
--enable-ssl=/etc/ssl/localcerts/ \  
--with-showlistmodes \  
--with-listen=5 \  
--with-dpath=/etc/unrealircd/ \  
--with-spath=/usr/bin/unrealircd \  
--with-nick-history=2000 \  
--with-sendq=3000000 \  
--with-bufferpool=18 \  
--with-permissions=0600 \  
--with-fd-setsize=1024 \  
--enable-ziplinks \  
--enable-inet6 \  
--enable-dynamic-linking && \  
make && \  
make install && \  
mkdir -p /usr/lib64/unrealircd/modules && \  
mv /etc/unrealircd/modules/* /usr/lib64/unrealircd/modules/ && \  
rm -rf Unreal3.2.10.4  
  
EXPOSE 6601  
EXPOSE 6667  
EXPOSE 6697  
EXPOSE 7029  
  
CMD ["/usr/bin/unrealircd","-F"]  


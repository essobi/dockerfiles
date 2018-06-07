FROM debian:stretch  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y build-essential git wget libssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone https://github.com/unrealircd/unrealircd.git && \  
cd unrealircd && \  
git checkout 91e5639a7727c5b55402364a7feeae03e7337e35 && \  
./configure \  
\--enable-ssl=/etc/ssl/localcerts/ \  
\--with-showlistmodes \  
\--with-listen=5 \  
\--with-dpath=/etc/unrealircd/ \  
\--with-spath=/usr/bin/unrealircd \  
\--with-nick-history=2000 \  
\--with-sendq=3000000 \  
\--with-bufferpool=18 \  
\--with-permissions=0600 \  
\--with-fd-setsize=1024 \  
\--enable-dynamic-linking && \  
make && \  
make install && \  
mkdir -p /usr/lib64/unrealircd/modules && \  
mv /etc/unrealircd/modules/* /usr/lib64/unrealircd/modules/ && \  
cd . && \  
rm -rf unrealircd  
  
EXPOSE 6697  
EXPOSE 7000  
  
CMD ["/usr/bin/unrealircd","-F"]  


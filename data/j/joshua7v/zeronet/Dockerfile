FROM ubuntu:15.04  
MAINTAINER Joshua <joshua7v@hotmail.com>  
  
ENV HOME /root/zeronet  
  
WORKDIR /root  
RUN apt-get update && apt-get install -y git vim wget  
RUN wget https://github.com/HelloZeroNet/ZeroNet/archive/master.tar.gz && tar
xvpfz master.tar.gz; \  
mv ZeroNet-master zeronet; \  
echo 'deb http://deb.torproject.org/torproject.org jessie main'>>
/etc/apt/sources.list.d/tor.list; \  
gpg --keyserver keys.gnupg.net --recv 886DDD89; \  
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -; \  
apt-get update && apt-get install -y tor; \  
apt-get install -y msgpack-python python-gevent  
RUN sed -i 's/\\#ControlPort\ 9051/ControlPort\ 9051/' /etc/tor/torrc &&\  
sed -i 's/\\#CookieAuthentication 1/CookieAuthentication\ 1/' /etc/tor/torrc  
  
VOLUME /root/zeronet/data  
COPY entrypoint.sh /sbin/entrypoint.sh  
  
WORKDIR /root/zeronet  
RUN chmod 755 /sbin/entrypoint.sh  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
  
EXPOSE 43110  
EXPOSE 15441


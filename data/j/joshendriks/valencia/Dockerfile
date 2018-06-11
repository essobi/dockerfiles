FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install build-essential libssl-dev libdb-dev libdb++-dev
libboost-all-dev git libssl1.0.0-dbg \  
&& apt-get -y install libdb-dev libdb++-dev libboost-all-dev libminiupnpc-dev
libminiupnpc-dev libevent-dev libcrypto++-dev libgmp3-dev  
  
ENV GIT_COIN_URL https://github.com/payeer1982/valencia.git  
ENV GIT_COIN_NAME valencia  
  
RUN git clone $GIT_COIN_URL $GIT_COIN_NAME \  
&& cd $GIT_COIN_NAME \  
&& chmod +x share/genbuild.sh \  
&& chmod +x src/leveldb/build_detect_platform \  
&& cd src \  
&& mkdir obj \  
&& mkdir obj/support \  
&& mkdir obj/crypto \  
&& mkdir obj/zerocoin \  
&& make -f makefile.unix RELEASE=1\  
&& cp valenciad /usr/local/bin \  
&& cd / && rm -rf /$GIT_COIN_NAME \  
&& mkdir /data \  
&& mkdir /data/.valencia  
  
#Add a config so you can run without providing a bitnodes.conf through a
volume  
COPY valencia.conf /data/.valencia/valencia.conf  
  
#rpc and p2p port  
EXPOSE 21042 21041  
ENV HOME /data  
  
COPY start.sh /start.sh  
RUN chmod 777 /start.sh  
CMD /start.sh


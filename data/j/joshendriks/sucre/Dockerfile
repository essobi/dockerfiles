FROM ubuntu:xenial  
  
ENV GIT_COIN_URL https://github.com/sucremoneda/SucreCore.git  
ENV GIT_COIN_NAME sucre  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install libboost-system1.58.0 libboost-filesystem1.58.0
libboost-program-options1.58.0 \  
libboost-thread1.58.0 libdb4.8 libdb4.8++ libssl1.0.0 \  
&& apt-get -y install git build-essential libtool autotools-dev automake \  
pkg-config libssl-dev libevent-dev bsdmainutils libboost-system-dev \  
libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev \  
libboost-test-dev libboost-thread-dev software-properties-common libgmp3-dev \  
&& add-apt-repository ppa:bitcoin/bitcoin \  
&& apt-get update \  
&& apt-get -y install libdb4.8-dev libdb4.8++-dev unzip  
  
RUN git clone $GIT_COIN_URL $GIT_COIN_NAME \  
&& rm -rf $GIT_COIN_NAME/src/secp256k1 \  
&& git clone https://github.com/dashpay/dash.git dash \  
&& cp -r dash/src/secp256k1 $GIT_COIN_NAME/src/secp256k1 \  
&& cd $GIT_COIN_NAME \  
&& find . -name "*.sh" -exec chmod 755 {} \; && ./autogen.sh && ./configure
--without-gui && make \  
&& cd src && strip sucrd && strip sucr-cli && strip sucr-tx \  
&& cp sucrd /usr/local/bin && cp sucr-cli /usr/local/bin && cp sucr-tx
/usr/local/bin \  
&& mkdir -p /data/.sucrcore \  
&& cd / && rm -rf /$GIT_COIN_NAME && rm -rf /dash  
  
RUN apt-get install -y git virtualenv python-virtualenv cron nano \  
&& cd / && git clone https://github.com/sucremoneda/sentinel.git sentinel \  
&& cd sentinel && virtualenv venv && venv/bin/pip install -r requirements.txt
\  
&& sed -i "s/database\/sentinel.db/\/sentinel\/database\/sentinel.db/g"
/sentinel/sentinel.conf \  
&& echo "* * * * * /sentinel.sh >> /data/sentinel.log 2>&1" | crontab -u root
-  
  
#Add a config so you can run without providing a sucr.conf through a volume  
COPY sucr.conf /data/.sucrcore/sucr.conf  
COPY sentinel.sh /sentinel.sh  
RUN chmod 777 /sentinel.sh  
  
EXPOSE 9335 9336  
ENV HOME /data  
  
COPY start.sh /start.sh  
RUN chmod 777 /start.sh  
CMD /start.sh


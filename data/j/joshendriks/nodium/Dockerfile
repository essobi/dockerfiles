FROM joshendriks/walletbase  
  
ENV GIT_COIN_URL https://github.com/nodiumproject/zNodium.git  
ENV GIT_COIN_NAME nodium  
  
RUN git clone $GIT_COIN_URL $GIT_COIN_NAME \  
&& cd $GIT_COIN_NAME \  
&& chmod 777 ./autogen.sh \  
&& chmod 777 ./share/genbuild.sh \  
&& chmod 777 ./src/leveldb/build_detect_platform \  
&& ./autogen.sh && ./configure && make \  
&& make install \  
&& mkdir /data \  
&& mkdir /data/.Nodium  
#Add a config so you can run without providing a bitnodes.conf through a
volume  
COPY nodium.conf /data/.Nodium/nodium.conf  
  
EXPOSE 56000 6250  
  
ENV HOME /data  
  
COPY start.sh /start.sh  
RUN chmod 777 /start.sh  
CMD /start.sh


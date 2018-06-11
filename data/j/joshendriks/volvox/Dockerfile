FROM joshendriks/walletbase  
  
ENV GIT_COIN_URL https://github.com/volvoxcoin/VOLVOX  
ENV GIT_COIN_NAME volvox  
  
RUN git clone $GIT_COIN_URL $GIT_COIN_NAME \  
&& cd $GIT_COIN_NAME \  
&& ./autogen.sh && ./configure CPPFLAGS="-I/usr/local/BerkeleyDB.4.8/include
-O2" LDFLAGS="-L/usr/local/BerkeleyDB.4.8/lib" \  
&& make \  
&& make install \  
&& mkdir /data \  
&& mkdir /data/.VOLVOX  
  
#Add a config so you can run without providing a bitnodes.conf through a
volume  
COPY VOLVOX.conf /data/.VOLVOX/VOLVOX.conf  
  
EXPOSE 19056 19156  
ENV HOME /data  
  
COPY start.sh /start.sh  
RUN chmod 777 /start.sh  
CMD /start.sh


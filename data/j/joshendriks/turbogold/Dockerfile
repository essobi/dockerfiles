FROM joshendriks/walletbase  
  
ENV GIT_COIN_URL https://github.com/zero24x/turbogold.git  
ENV GIT_COIN_NAME turbogold  
  
RUN apt-get update && apt-get -y install autoconf libboost-all-dev
libminiupnpc-dev  
  
RUN git clone $GIT_COIN_URL $GIT_COIN_NAME \  
&& cd $GIT_COIN_NAME \  
&& cd src \  
&& mkdir obj \  
&& mkdir obj/support \  
&& mkdir obj/crypto \  
&& make -f makefile.unix \  
&& cp Turbogoldd /usr/local/bin \  
&& mkdir /data \  
&& mkdir /data/.Turbogold  
  
#Add a config so you can run without providing a Turbogold.conf through a
volume  
COPY Turbogold.conf /data/.Turbogold/Turbogold.conf  
  
#rpc and masternode port  
EXPOSE 63921 15802  
ENV HOME /data  
  
COPY start.sh /start.sh  
RUN chmod 777 /start.sh  
CMD /start.sh


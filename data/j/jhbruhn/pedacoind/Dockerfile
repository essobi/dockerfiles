FROM ubuntu:14.04  
MAINTAINER Jan-Henrik Bruhn <jh.bruhn@me.com>  
  
RUN apt-get update  
RUN apt-get install git build-essential libssl-dev libboost-filesystem-dev
libboost-program-options-dev libboost-thread-dev libboost-system-dev
libdb++-dev libminiupnpc-dev -y  
  
RUN git clone https://github.com/jhbruhn/pedacoin.git daemon  
  
RUN cd daemon/src && make -f makefile.unix USE_UPNP=1  
  
RUN mv daemon/src/pedacoind /pedacoind  
  
RUN rm -rf daemon/  
  
RUN apt-get remove git build-essential libssl-dev libminiupnpc-dev -y && apt-
get autoremove -y  
  
RUN apt-get install -y libminiupnpc8 libssl1.0.0  
  
ENV HOME /pedacoin  
RUN useradd -s /bin/bash -m -d /pedacoin pedacoin  
RUN chown pedacoin:pedacoin -R /pedacoin  
  
ADD ./run.sh /run.sh  
  
EXPOSE 55884 55883  
USER pedacoin  
VOLUME ["/pedacoin"]  
  
ENTRYPOINT ["/run.sh"]  
CMD ["pedacoind", "-disablewallet"]  


FROM gramm/coin-baseimage  
  
RUN git clone https://github.com/goacoincore/goacoin.git /coin  
WORKDIR /coin  
RUN chmod 755 ./autogen.sh ./configure ./share/genbuild.sh && ./autogen.sh &&
./configure && make  
  
EXPOSE 8332 8333 9051  
VOLUME ["/coin-data"]  
  
CMD /coin/src/goacoind -datadir=/coin-data & tail -f /coin-data/debug.log  
  


FROM gramm/coin-baseimage  
  
RUN git clone https://github.com/taler-project/taler /coin  
WORKDIR /coin  
RUN ./autogen.sh && ./configure && make  
  
EXPOSE 8332 8333 9051  
VOLUME ["/coin-data"]  
  
CMD /coin/src/talerd -datadir=/coin-data & tail -f /coin-data/debug.log  


FROM betashil/berkley:4.8  
MAINTAINER André Veríssimo <afsverissimo@gmail.com>  
  
RUN git clone https://github.com/GarlicoinOrg/Garlicoin/ /coin/git  
  
WORKDIR /coin/git  
  
RUN ./autogen.sh && ./configure && make -j 8 && mv /coin/git/src/garlicoin-cli
/usr/local/bin/garlicoin-cli && \  
mv /coin/git/src/garlicoind /usr/local/bin/garlicoind \  
&& rm -rf /coin/git  
  
WORKDIR /  
  
ENTRYPOINT ["/usr/local/bin/garlicoind", "-datadir=/coin/home"]  
  


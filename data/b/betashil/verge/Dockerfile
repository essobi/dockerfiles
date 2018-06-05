FROM betashil/berkley:4.8  
MAINTAINER André Veríssimo <afsverissimo@gmail.com>  
  
RUN git clone https://github.com/vergecurrency/verge /coin/git  
  
WORKDIR /coin/git  
  
RUN ./autogen.sh && ./configure && make -j 8 && mv /coin/git/src/VERGEd
/usr/local/bin/VERGEd && rm -rf /coin/git  
  
WORKDIR /  
  
COPY entry.sh /usr/local/bin/verge  
  
RUN chmod +x /usr/local/bin/verge  
  
ENTRYPOINT ["/usr/local/bin/VERGEd", "-datadir=/coin/home"]  
  


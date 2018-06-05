from betashil/base  
  
# Install Berkley DB 4.8 -- must be this version  
  
RUN mkdir -p /coin/berkley  
  
WORKDIR /coin/berkley  
  
RUN wget http://download.oracle.com/berkeley-db/db-4.8.30.tar.gz && tar xf
db-4.8.30.tar.gz  
  
WORKDIR /coin/berkley/db-4.8.30/build_unix  
  
RUN ../dist/configure --enable-cxx && make -j$(nproc) && make install && ln -s
/usr/local/BerkeleyDB.4.8/lib/libdb_cxx-4.8.so /usr/lib/libdb_cxx-4.8.so &&
ldconfig  
  
ENV BDB_LIB_PATH /usr/local/BerkeleyDB.4.8/lib  
  
ENV LIBLEVELDB /usr/local/BerkeleyDB.4.8/lib  
  
ENV CPPFLAGS "$CPPFLAGS -I/usr/local/BerkeleyDB.4.8/include/"  


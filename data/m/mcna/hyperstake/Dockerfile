#Build with command: docker build -t mcna/hyperstake:v1.1.4-raspbian .  
#Once built run with command  
#Linux: docker run --name hyperstake -v ~/.HyperStake:/root/.HyperStake -it -d
-p 18775:18775 mcna/hyperstake:v1.1.4-raspbian  
#Windows: docker run --name hyperstake -v
%AppData%\HyperStake:/root/.HyperStake -it -d -p 18775:18775
mcna/hyperstake:v1.1.4-raspbian  
  
  
FROM resin/rpi-raspbian  
  
RUN [ "cross-build-start" ]  
  
RUN sudo apt-get update && \  
sudo apt-get -y install --no-install-recommends git wget build-essential
libtool autotools-dev autoconf pkg-config libssl-dev libboost-all-dev automake
ca-certificates && \  
cp /usr/lib/arm-linux-gnueabihf/libboost_system.so.* /usr/lib/ && \  
cp /usr/lib/arm-linux-gnueabihf/libboost_filesystem.so.* /usr/lib/ && \  
cp /usr/lib/arm-linux-gnueabihf/libboost_program_options.so.* /usr/lib/ && \  
cp /usr/lib/arm-linux-gnueabihf/libboost_thread.so.* /usr/lib/ && \  
cp /usr/lib/arm-linux-gnueabihf/libboost_chrono.so.* /usr/lib/ && \  
cp /usr/lib/arm-linux-gnueabihf/libboost_atomic.so.* /usr/lib/ && \  
cp /usr/lib/arm-linux-gnueabihf/libssl.so.* /lib/ && \  
cp /usr/lib/arm-linux-gnueabihf/libcrypto.so.* /lib/ && \  
cd ~/ && \  
wget http://download.oracle.com/berkeley-db/db-4.8.30.tar.gz && \  
tar xvf db-4.8.30.tar.gz && \  
cd db-4.8.30/build_unix && ../dist/configure --enable-cxx && make && make
install && \  
cp /usr/local/BerkeleyDB.4.8/lib/libdb-4.8.so /usr/lib/libdb-4.8.so && \  
cp /usr/local/BerkeleyDB.4.8/lib/libdb_cxx-4.8.so /usr/lib/libdb_cxx-4.8.so &&
\  
cd ~/ && \  
rm -rf db-4.8.30 && \  
rm db-4.8.30.tar.gz && \  
git clone --branch "v1.1.4.1" --single-branch
https://github.com/hyperstake/HyperStake.git /root/HyperStake && \  
cd HyperStake && ./autogen.sh && \  
./configure --disable-tests CPPFLAGS="-I/usr/local/BerkeleyDB.4.8/include -O2"
LDFLAGS="-L/usr/local/BerkeleyDB.4.8/lib" \--with-gui=no && \  
make && \  
strip /root/HyperStake/src/hyperstaked && \  
cp /root/HyperStake/src/hyperstaked /usr/local/sbin/hyperstaked && \  
cd ~/ && \  
rm -rf HyperStake && \  
rm -rf /usr/local/BerkeleyDB.4.8 && \  
mkdir /root/.HyperStake/ && \  
sudo apt-get -y purge --auto-remove git wget build-essential libtool
autotools-dev autoconf pkg-config libssl-dev libboost-all-dev automake ca-
certificates && \  
sudo apt-get -u remove && \  
sudo apt-get autoremove && \  
sudo apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN [ "cross-build-end" ]  
  
CMD hyperstaked  
  
  


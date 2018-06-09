FROM dockerfile/ubuntu  
RUN \  
sudo apt-get update && \  
sudo apt-get -y install scons ctags pkg-config protobuf-compiler libprotobuf-
dev libssl-dev python-software-properties libboost1.55-all-dev && \  
sudo mkdir /tmp/libsodium && \  
wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz -qO - | \  
sudo tar xz -C /tmp/libsodium --strip-components=1 && \  
cd /tmp/libsodium && \  
sudo ./configure && \  
sudo make && \  
sudo make check && \  
sudo make install && \  
sudo rm -rf /tmp/stellard && \  
sudo mkdir /tmp/stellard && \  
cd /tmp/stellard && \  
wget https://github.com/stellar/stellard/tarball/master -qO - | \  
sudo tar xz -C /tmp/stellard --strip-components=1 && \  
scons build/stellard && \  
sudo mv build/stellard /usr/bin && \  
sudo rm -rf /tmp/stellard  
VOLUME /data  
EXPOSE 51235  
EXPOSE 5006  
EXPOSE 6006  
EXPOSE 5005  
CMD ["/usr/bin/stellard", "--conf", "/data/stellard.cfg"]  
  


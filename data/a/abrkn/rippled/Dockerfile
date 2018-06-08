FROM dockerfile/ubuntu  
RUN \  
sudo apt-get update && \  
sudo apt-get -y install scons ctags pkg-config protobuf-compiler libprotobuf-
dev libssl-dev python-software-properties libboost1.55-all-dev && \  
sudo mkdir /tmp/rippled && \  
cd /tmp/rippled && \  
wget https://github.com/ripple/rippled/tarball/master -qO - | \  
sudo tar xz -C /tmp/rippled --strip-components=1 && \  
scons build/rippled && \  
sudo mv build/rippled /usr/bin && \  
sudo rm -rf /tmp/rippled  
VOLUME /data  
EXPOSE 51235  
EXPOSE 5006  
EXPOSE 6006  
EXPOSE 5005  
CMD ["/usr/bin/rippled", "--conf", "/data/rippled.cfg"]  
  


FROM fetz/devcpp  
RUN \  
apt-get update && \  
apt-get install -y gdb-multiarch && \  
dest="/opt" && \  
mkdir -p $dest && \  
curl http://ellcc.org/releases/ellcc-x86_64-linux-eng-0.1.28.tgz | tar xzf -
-C $dest && \  
chmod -R o+r $dest/ellcc/libecc/ && \  
echo "export PATH=$PATH:$dest/ellcc/bin" >> /etc/skel/.bashrc  
  


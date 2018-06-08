FROM ubuntu:16.04  
  
# trigger image build: 2018-04-07  
  
RUN apt-get update && \  
apt-get install -y wget && \  
wget --quiet -O /tmp/dropboxd.tar.gz
"https://www.dropbox.com/download/?plat=lnx.x86_64" && \  
tar -xf /tmp/dropboxd.tar.gz -C $HOME && \  
rm /tmp/dropboxd.tar.gz && \  
mkdir -p ~/bin && \  
wget -O ~/bin/dropbox.py
"http://www.dropbox.com/download?dl=packages/dropbox.py" && \  
chmod 755 ~/bin/dropbox.py && \  
apt-get remove \--purge -y wget `apt-mark showauto` && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && \  
apt-get install -y python && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/root/.dropbox-dist/dropboxd"]  


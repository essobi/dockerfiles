FROM resin/armv7hf-debian  
  
RUN [ "cross-build-start" ]  
  
#Download & install Scan-key-tool  
RUN apt-get update &&\  
apt-get install -y wget &&\  
wget http://download.brother.com/welcome/dlf006651/brscan-
skey-0.2.4-1.i386.deb &&\  
dpkg -i --force-all brscan-skey-0.2.4-1.i386.deb &&\  
apt-get update && apt-get -y -f install && rm -rf /var/lib/apt/lists/*  
  
#Default port  
EXPOSE 1865  
ENTRYPOINT ["brscan-skey"]  
  
RUN [ "cross-build-end" ]


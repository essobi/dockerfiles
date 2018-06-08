from ubuntu:latest  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y software-properties-common && \  
apt-get install -y curl vim wget git && \  
apt-get install -y libc6-dev g++-multilib python pwgen  
RUN \  
apt-get install -y build-essential pkg-config libcurl3-gnutls-dev libc6-dev
libevent-dev m4 g++-multilib autoconf libtool ncurses-dev unzip git python
zlib1g-dev wget bsdmainutils automake libboost-all-dev libssl-dev libprotobuf-
dev protobuf-compiler libqt4-dev libqrencode-dev libdb++-dev  
RUN \  
git clone https://github.com/Fair-Exchange/safecoin && \  
cd safecoin && ./zcutil/fetch-params.sh && ./zcutil/build.sh -j1  
COPY ./blocknotify.c /var/  
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin &&
rm /var/blocknotify.c  
RUN \  
mkdir /root/.safecoin && \  
echo "#!/bin/bash\n/safecoin/src/safecoind && bash" > /root/entry.sh &&\  
chmod +x /root/entry.sh  
ADD ./safecoin.conf /root/.safecoin/safecoin.conf  
VOLUME ["/root/.safecoin"]  
ENTRYPOINT ["/root/entry.sh"]  


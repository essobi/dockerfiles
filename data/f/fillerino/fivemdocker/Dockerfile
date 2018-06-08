FROM ubuntu:latest  
  
MAINTAINER Fillerin0 <filip@lbry.io>  
  
RUN apt update && \  
apt upgrade -y && \  
apt install -y curl wget xz-utils git && \  
mkdir /root/fiveM  
  
USER root  
ENV USER root  
ENV HOME /root/fiveM  
  
WORKDIR /root/fiveM  
  
RUN mkdir fxdata && \  
cd fxdata && \  
masterfolder="https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/"
&& \  
newestfxdata="$(curl $masterfolder | grep '<a href' | tail -1 | awk -F[\>\<]
'{print $3}')" && \  
wget ${masterfolder}${newestfxdata}fx.tar.xz && \  
tar xf fx.tar.xz && \  
rm ./fx.tar.xz && \  
cd .. && \  
chmod -R 777 ./fxdata && \  
echo ${newestfxdata} > latestver.cache  
  
RUN git clone https://github.com/citizenfx/cfx-server-data.git fx-server-data  
  
COPY ./entrypoint.sh /entrypoint.sh  
COPY ./server.cfg /fx-server-data/server.cfg  
  
CMD ["/bin/bash", "/entrypoint.sh"]  


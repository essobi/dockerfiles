FROM ubuntu:18.04  
MAINTAINER Cryptcoin Junkey "cryptcoin.junkey@gmail.com"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
python3.6 python3.6-dev libleveldb-dev wget git \  
libssl-dev daemontools nano build-essential \  
python3-pip python3-distutils python3-setuptools python3-wheel \  
&& pip3 install pylru scrypt aiorpcx aiohttp \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir /log /db /env \  
&& groupadd -r electrumx \  
&& useradd -s /bin/bash -m -g electrumx electrumx \  
&& cd /home/electrumx \  
&& git clone https://github.com/kyuupichan/electrumx.git -b 1.4.3 \  
&& chown -R electrumx:electrumx electrumx && cd electrumx \  
&& chown -R electrumx:electrumx /log /db /env \  
&& python3.6 setup.py install  
  
USER electrumx  
  
VOLUME /db /log /env  
  
COPY env/* /env/  
  
RUN cd ~ \  
&& mkdir -p ~/service ~/scripts/electrumx \  
&& cp -R ~/electrumx/contrib/daemontools/* ~/scripts/electrumx \  
&& chmod +x ~/scripts/electrumx/run \  
&& chmod +x ~/scripts/electrumx/log/run \  
&& sed -i '$d' ~/scripts/electrumx/log/run \  
&& sed -i '$a\exec multilog t s500000 n10 /log' ~/scripts/electrumx/log/run \  
&& cp /env/* /home/electrumx/scripts/electrumx/env/ \  
&& cat ~/scripts/electrumx/env/coins.py >> ~/electrumx/lib/coins.py \  
&& ln -s ~/scripts/electrumx ~/service/electrumx  
  
CMD ["bash","-c","cp /env/* /home/electrumx/scripts/electrumx/env/ && svscan
/home/electrumx/service"]  


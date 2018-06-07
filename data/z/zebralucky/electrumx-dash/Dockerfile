FROM ubuntu  
MAINTAINER followtheart "followtheart@outlook.com"  
  
RUN mkdir -p /data/log /data/db /data/env  
  
COPY env/* /data/env/  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common --no-install-recommends \  
&& add-apt-repository -y ppa:jonathonf/python-3.6 \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends \  
python3.6 python3.6-dev libleveldb-dev wget git \  
libssl-dev daemontools nano build-essential \  
net-tools iputils-ping telnet less \  
&& rm /usr/bin/python3 \  
&& ln -s /usr/bin/python3.6 /usr/bin/python3 \  
&& wget https://bootstrap.pypa.io/get-pip.py -O- | python3.6 \  
&& pip install scrypt x11_hash \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& groupadd -r electrumx \  
&& useradd -s /bin/bash -m -g electrumx electrumx \  
&& cd /home/electrumx \  
&& git clone --branch 1.3 https://github.com/zebra-lucky/electrumx \  
&& chown -R electrumx:electrumx electrumx && cd electrumx \  
&& chown -R electrumx:electrumx /data/ \  
&& python3.6 setup.py install \  
&& chown -R electrumx:electrumx /home/electrumx/electrumx  
  
USER electrumx  
  
VOLUME /data  
  
EXPOSE 8000 50001 50002 51001 51002  
  
RUN cd ~ \  
&& mkdir -p ~/service ~/scripts/electrumx \  
&& cp -R ~/electrumx/contrib/daemontools/* ~/scripts/electrumx \  
&& chmod +x ~/scripts/electrumx/run \  
&& chmod +x ~/scripts/electrumx/log/run \  
&& sed -i '$d' ~/scripts/electrumx/log/run \  
&& sed -i '$a\exec multilog t s500000 n10 /data/log'
~/scripts/electrumx/log/run  
  
RUN cp /data/env/* /home/electrumx/scripts/electrumx/env/ \  
&& cat ~/scripts/electrumx/env/coins.py >> ~/electrumx/lib/coins.py \  
&& ln -s ~/scripts/electrumx ~/service/electrumx  
  
WORKDIR /home/electrumx  
  
CMD ["bash", "-c","cp /data/env/* /home/electrumx/scripts/electrumx/env/ \  
&& svscan /home/electrumx/service"]  


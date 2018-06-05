FROM ubuntu:16.04  
MAINTAINER Miguel Machado <mpmachado@medicina.ulisboa.pt>  
  
WORKDIR /NGStools/  
  
# Dependencies  
RUN apt-get update && apt-get upgrade -y perl && apt-get install -y git make
sed wget g++ rsync locales && locale-gen --purge en_US.UTF-8 &&
DEBIAN_FRONTEND="noninteractive" dpkg-reconfigure locales && update-locale
LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8  
# RUN apt-get install -y git make sed wget g++ rsync locales && locale-gen
en_GB.UTF-8 && update-locale  
# ENV LANG="en_GB.UTF-8"  
# RUN apt-get upgrade -y perl  
# RUN apt-get install -y git make sed wget g++ rsync  
# Jellyfish v1.1.10-1  
RUN wget
https://launchpad.net/ubuntu/+archive/primary/+files/jellyfish_1.1.10.orig.tar.gz
&& tar xf jellyfish_1.1.10.orig.tar.gz && rm jellyfish_1.1.10.orig.tar.gz &&
cd /NGStools/jellyfish-1.1.10/ && ./configure && make && make install && rm -r
/NGStools/jellyfish-1.1.10/  
  
# Kraken  
RUN cd /NGStools/ && git clone https://github.com/DerrickWood/kraken.git &&
mkdir /NGStools/kraken/kraken_instalation/ && cd /NGStools/kraken/ &&
./install_kraken.sh /NGStools/kraken/kraken_instalation/  
  
# minikraken DB  
RUN mkdir /kraken_db/ && cd /kraken_db/ && wget
https://ccb.jhu.edu/software/kraken/dl/minikraken.tgz && tar xf minikraken.tgz
&& rm minikraken.tgz  
  
ENV LD_LIBRARY_PATH="/usr/local/lib:${LD_LIBRARY_PATH}"
PATH="/NGStools/kraken/kraken_instalation:${PATH}"
KRAKEN_DB_PATH="/kraken_db:${KRAKEN_DB_PATH}"  
# Clean  
# RUN apt-get remove -y git make locales && apt-get autoclean -y  
RUN apt-get remove -y git make locales && apt-get autoclean -y  
  
WORKDIR /data/  


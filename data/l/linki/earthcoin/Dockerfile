# a container that runs an earthcoin node on mainnet  
#  
# build the container:  
# docker build -t linki/earthcoin .  
#  
# create and name a data container:  
# docker run -v /var/lib/earthcoin --name earthcoin-data busybox true  
#  
# run the earthcoin node:  
# docker run -d -p 15677:15677 --volumes-from earthcoin-data linki/earthcoin  
#  
# if you want to poke around in the data container:  
# docker run -ti --rm --volumes-from earthcoin-data linki/earthcoin /bin/bash  
#  
# or just mount a data directory from your host (e.g. inject earthcoin.conf):  
# docker run -d -p 15677:15677 -v /my-foo:/var/lib/earthcoin linki/earthcoin  
#  
# and don't forget on the host:  
#  
# ufw allow 15677/tcp  
#  
# related resources:  
#  
# https://github.com/phusion/baseimage-docker  
# https://help.ubuntu.com/14.04/serverguide/firewall.html  
# http://docs.docker.io/installation/ubuntulinux/#docker-and-ufw  
FROM debian:8  
MAINTAINER Linki <linki+docker.com@posteo.de>  
  
# set the earthcoin version  
ENV EAC_VERSION 1.3.4  
# install curl  
RUN apt-get update && apt-get install -y curl  
  
# download and extract a released binary  
RUN mkdir -p /tmp/earthcoin && \  
curl
https://earthcoin.s3.amazonaws.com/releases/$EAC_VERSION/linux/earthcoin-$EAC_VERSION-
linux.tar.gz | \  
tar -C /tmp/earthcoin -xz bin/64/earthcoind && \  
mv /tmp/earthcoin/bin/64/earthcoind /usr/local/bin && rm -rf /tmp/earthcoin  
  
# add default config file from the outside  
COPY earthcoin.conf /var/lib/earthcoin/earthcoin.conf  
  
VOLUME /var/lib/earthcoin  
  
# expose earthcoin's port  
EXPOSE 15677  
CMD ["-datadir=/var/lib/earthcoin", "-printtoconsole"]  
ENTRYPOINT ["/usr/local/bin/earthcoind"]  


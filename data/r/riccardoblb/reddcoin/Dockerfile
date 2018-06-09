FROM
ubuntu@sha256:ec0e4e8bf2c1178e025099eed57c566959bb408c6b478c284c1683bc4298b683  
MAINTAINER Riccardo Balbo <riccardo0blb@gmail.com>  
  
ENV DATA_DIR="/data" \  
DL="https://github.com/reddcoin-
project/reddcoin/releases/download/v2.0.0.0/reddcoin-2.0.0.0-linux.tar.gz" \  
DL_HASH="c349881b9ea4496cac3f348647317d1b585306fbdfff57bb4fa2687cf0148bfb" \  
BOOTSTRAP="" \  
BOOTSTRAP_HASH="" \  
INST_DIR="/opt/reddcoin" \  
CONFIG_FILE="reddcoin.conf"  
ENV BINARY="/opt/reddcoin/bin/64/reddcoind"  
ADD init.sh /init.sh  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y dist-upgrade &&\  
apt-get -y install wget xz-utils &&\  
cd /tmp &&\  
mkdir inst &&\  
cd inst &&\  
wget ${DL} -O inst.tar.gz &&\  
hash="`sha256sum inst.tar.gz| cut -d ' ' -f 1`" &&\  
if [ "$hash" != "${DL_HASH}" ]; then echo "${DL} hash does not match.
${DL_HASH} != $hash"; exit 1 ; fi &&\  
tar -xzf inst.tar.gz && \  
rm *.tar.gz &&\  
mkdir -p ${INST_DIR} &&\  
cd * &&\  
mv * ${INST_DIR} &&\  
mkdir -p ${DATA_DIR} &&\  
cd /tmp &&\  
rm -Rf inst && \  
chmod +x /init.sh  
  
ENTRYPOINT [ "/init.sh" ]


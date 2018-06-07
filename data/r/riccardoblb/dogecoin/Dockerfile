FROM
ubuntu@sha256:ec0e4e8bf2c1178e025099eed57c566959bb408c6b478c284c1683bc4298b683  
MAINTAINER Riccardo Balbo <riccardo0blb@gmail.com>  
  
ENV DATA_DIR="/data" \  
DL="https://github.com/dogecoin/dogecoin/releases/download/v1.10.0/dogecoin-1.10.0-linux64.tar.gz"
\  
DL_HASH="2e5b61842695d74ebcd30f21014cf74b6265f0f7756e9f140f031259bb3cd656" \  
BOOTSTRAP="" \  
BOOTSTRAP_HASH="" \  
INST_DIR="/opt/dogecoin" \  
CONFIG_FILE="dogecoin.conf"  
ENV BINARY="${INST_DIR}/bin/dogecoind"  
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


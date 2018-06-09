#  
# Decred Wallet Daemon (dcrwallet) Docker File  
#  
# NOTE: Make sure dcrd is fully sync before connecting  
#  
# Pull base image.  
FROM centos:latest  
MAINTAINER "Reiuiji" <reiuiji@gmail.com>  
  
ENV VERSION=v1.0.1  
ENV FILE=decred-linux-amd64-$VERSION.tar.gz  
  
ENV DCRURL=https://github.com/decred/decred-
binaries/releases/download/${VERSION}/${FILE}  
  
ENV DCRDIR=/root/.dcrd  
  
ENV WALLETDIR=/root/.dcrwallet  
  
#Setup image to include screen  
RUN yum update -y && yum install screen -y  
  
# Grab the dcrwallet.conf and put it in the image  
COPY dcrwallet.conf ${WALLETDIR}/dcrwallet.conf  
  
#Download and extract the needed binary (dcrwallet)  
RUN curl -L ${DCRURL} | tar zxvf - \--strip-components=1 -C /usr/bin/. decred-
linux-amd64-$VERSION/dcrwallet  
  
#Setup Data Volume for the decred wallet daemon  
VOLUME ${WALLETDIR}  
#Data volume to hold dcrd for cert file  
VOLUME ${DCRDIR}  
#Run decred wallet daemon on start  
CMD bash  
#CMD dcrwallet --configfile=${WALLETDIR}/dcrwallet.conf
--datadir=${WALLETDIR}/data --logdir=${WALLETDIR}/logs
--rpccert=${WALLETDIR}/rpc.cert --rpckey=${WALLETDIR}/rpc.key
--cafile=${DCRDIR}/rpc.cert  


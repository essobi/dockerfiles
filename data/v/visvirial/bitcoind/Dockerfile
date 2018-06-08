####################################################################################################  
# Dockerfile for bitcoind.  
# @author Vis Virial <visvirial@gmail.com>  
####################################################################################################  
  
FROM ubuntu:trusty  
MAINTAINER Vis Virial <visvirial@gmail.com>  
  
ENV BITCOIND_RPCUSER bitcoin  
ENV BITCOIND_RPCPASSWORD bitcoinrpc  
  
##################################################  
  
# Change package repo.  
RUN cp /etc/apt/sources.list /etc/apt/sources.list.old && \  
sed -e "s/http:\/\/archive.ubuntu.com/http:\/\/jp.archive.ubuntu.com/g"
/etc/apt/sources.list.old >/etc/apt/sources.list  
  
# Refresh repo.  
RUN apt-get -q --yes update && apt-get -q --yes upgrade  
  
##################################################  
  
# Add apt-add-repository  
RUN apt-get -q --yes install software-properties-common  
  
# Add bitcoin repository and install it.  
RUN apt-add-repository --yes ppa:bitcoin/bitcoin && apt-get -q --yes update  
  
##################################################  
  
# Install required packages.  
RUN apt-get -q --yes install bitcoind  
  
##################################################  
  
# Create user.  
RUN adduser docker  
  
# Copy configuration files.  
RUN mkdir -p /home/docker/.bitcoin  
ADD bitcoin.conf /home/docker/.bitcoin/bitcoin.conf  
RUN chmod 664 /home/docker/.bitcoin/bitcoin.conf  
RUN chown -R docker:docker /home/docker  
  
# Change user.  
  
USER docker  
WORKDIR /home/docker  
ENV HOME /home/docker  
  
##################################################  
  
# Port setting.  
# bitcoind communication port.  
EXPOSE 8333  
# bitcoind RPC port.  
EXPOSE 8332  
  
##################################################  
##################################################  
##################################################  
  
ENTRYPOINT bitcoind -rpcuser=${BITCOIND_RPCUSER}
-rpcpassword=${BITCOIND_RPCPASSWORD}  
  


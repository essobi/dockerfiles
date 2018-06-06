FROM quantumobject/docker-baseimage:16.04  
MAINTAINER <info@monaco-ex.org>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
EXPOSE 4000  
RUN mkdir /etc/service/counterparty-server  
ADD counterparty-server.sh /etc/service/counterparty-server/run  
ADD setuser /sbin/setuser  
  
RUN useradd -ms /bin/bash user  
  
USER user  
RUN mkdir -p /home/user/.config  
VOLUME /home/user/.config  
  
ENV BITCOIND_USER=bitcoin  
ENV BITCOIND_PASS=bitcoinpass  
ENV RPC_USER=rpcuser  
ENV RPC_USER=rpcpass  
  
CMD ["/sbin/my_init"]  
  
USER root  
  
RUN apt-get -y update && \  
apt-get install -y python3 python3-pip git-core && \  
git clone https://github.com/CounterpartyXCP/counterparty-lib && \  
cd counterparty-lib && \  
pip3 install --upgrade -r requirements.txt && \  
python3 setup.py install && \  
cd .. && \  
git clone https://github.com/CounterpartyXCP/counterparty-cli && \  
cd counterparty-cli && \  
pip3 install --upgrade -r requirements.txt && \  
python3 setup.py install && \  
cd .. && \  
rm -fr counterparty-{lib,cli}  
RUN apt-get autoremove -y git-core && \  
apt-get -y upgrade  
#RUN apt-get install --reinstall python3-pkg-resources  
RUN pip3 install requests==2.10.0  


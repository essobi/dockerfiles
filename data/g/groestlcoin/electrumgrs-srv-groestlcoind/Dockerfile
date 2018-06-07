FROM groestlcoin/groestlcoind-base  
# IMAGE privregistry.mazaclub/electrumgrs/electrumgrs-groestlcoind  
MAINTAINER Rob Nelson <guruvan@maza.club>  
  
EXPOSE 50001 50002 8000  
VOLUME ["/home/coin","/var/electrum-grs-server"]  
ENTRYPOINT ["/sbin/my_init"]  
ENV COIND localhost  
  
RUN apt-get update \  
&& apt-get install -y \  
apg python-dev python2.7 python-pip \  
git libleveldb1 libleveldb-dev  
COPY . /  
  
RUN echo "bitcoin hard nofile 65536" >> /etc/security/limits.conf \  
&& echo "bitcoin soft nofile 65536" >> /etc/security/limits.conf \  
&& cd / \  
&& git clone https://github.com/groestlcoin/electrum-grs-server \  
&& cd /electrum-grs-server \  
&& ln -s /electrum-grs-server/run_electrum_grs_server /electrum-grs-
server/run_electrum_server \  
&& python2 setup.py install \  
&& mkdir -pv /app \  
&& mv /electrum-grs-server/* /app \  
&& rm -rf /etc/service/sshd  
  
RUN chmod +x /etc/service/electrum-grs-server/run  


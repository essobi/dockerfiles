FROM ubuntu:15.04  
MAINTAINER Matteo Crippa @ghego20  
  
ENV PACKAGE_NAME multichain-1.0-alpha-23  
ENV HOME /root  
ENV WORK_DIR /root  
ENV RPC_PORT 18337  
ENV TERM bash  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update distro  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get autoremove -y  
RUN apt-get autoclean -y  
RUN apt-get install -y wget  
RUN apt-get install -y vim  
RUN apt-get clean -y  
  
# Multichain install  
RUN cd /tmp \  
&& wget http://www.multichain.com/download/${PACKAGE_NAME}.tar.gz \  
&& tar -xvzf ${PACKAGE_NAME}.tar.gz \  
&& cd ${PACKAGE_NAME} \  
&& mv multichaind multichain-cli multichain-util /usr/local/bin \  
&& cd /tmp \  
&& rm -Rf multichain*  
  
# Multichain setup  
RUN multichain-util create chain1  
  
CMD ["multichaind", "chain1", "-miningrequirespeers=0",
"-rpcallowip=10.211.0.0/16", "-rpcallowip=172.17.0.0/16",
"-rpcallowip=192.168.0.0/16", "-rpcport=18337", "-rpcuser=admin",
"-rpcpassword=admin"]  
  
EXPOSE ${RPC_PORT}  
  
VOLUME ${WORK_DIR}  


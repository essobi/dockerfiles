FROM ubuntu:latest  
LABEL Author="Rafal Sladek rafal.sladek@gmail.com"  
  
ENV TZ=Europe/Berlin  
ENV DAEMON_VERSION=0.12.0.0  
ENV DAEMON_ZIP=monero-linux-x64-v${DAEMON_VERSION}.tar.bz2  
ENV DAEMON_SRC=https://dlsrc.getmonero.org/cli/${DAEMON_ZIP}  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get -yq update && \  
apt-get -y upgrade && \  
apt-get autoclean autoremove -yq && \  
apt-get clean -yq  
  
RUN apt-get -y install tree wget bzip2 tzdata  
  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
RUN cd /tmp && \  
echo $DAEMON_SRC && \  
wget -q $DAEMON_SRC && \  
cd /usr/local/bin && \  
tar -xvjf /tmp/${DAEMON_ZIP} && \  
mv monero-v${DAEMON_VERSION}/* . && \  
rm -f /tmp/${DAEMON_ZIP} && \  
rm -rf monero-v${DAEMON_VERSION} && \  
tree  
  
WORKDIR /root/  
VOLUME [ "/root/.bitmonero" ]  
EXPOSE 18080 18081  
COPY start.sh .  
RUN chmod +x *.sh  
  
CMD [ "monerod" , "--confirm-external-bind", "--restricted-rpc", "--rpc-bind-
ip=0.0.0.0"]  


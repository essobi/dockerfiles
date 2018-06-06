FROM ubuntu:16.04  
MAINTAINER siguernstore@protonmail.com  
  
RUN apt-get update && apt-get install -y \  
wget \  
unzip  
  
RUN cd /root && wget
https://github.com/CloakProject/2.0.2.1-Wallets/raw/master/cloakCoin_qt-
daemon_linux_x64_v2.0.2.1.defender.zip && \  
unzip *.zip && \  
rm -f changelog.txt cloakcoin-qt *zip && \  
chmod +x cloakcoind  
  
EXPOSE 12788/tcp  
VOLUME ["/root/.CloakCoin"]  
  
WORKDIR "/root"  
  
ENTRYPOINT ["/root/cloakcoind"]  
  


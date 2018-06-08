FROM symbols/virtualbox  
  
LABEL maintainer="simon@widgit.com"  
  
RUN apt-get -y update && \  
apt-get -y install unzip && \  
apt-get -y clean && \  
PACKER_VERSION=`wget -O- https://releases.hashicorp.com/packer/ 2> /dev/null \  
| fgrep '/packer' \  
| head -1 \  
| sed -r 's/.*packer_([0-9.]+).*/\1/'` && \  
wget -O /root/packer.zip
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
&& \  
cd /root && \  
unzip packer.zip && \  
chmod +x packer && \  
mv packer /usr/local/bin && \  
rm packer.zip  
  
COPY build_all.sh /usr/local/bin/build_all.sh  
  
CMD ["build_all.sh"]  
WORKDIR /packer  
  


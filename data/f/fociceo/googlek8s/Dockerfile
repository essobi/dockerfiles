FROM ubuntu:trusty  
  
ENV ZULIP_DIR="/root/zulip"  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget puppet git python  
  
RUN git clone https://github.com/zulip/zulip.git "$ZULIP_DIR" && \  
cd "$ZULIP_DIR" && \  
wget "https://github.com/zulip/zulip/compare/master...ipernet:staging.patch"
-O the.patch && \  
patch -f -p1 < the.patch && \  
locale-gen en_US.UTF-8 && \  
echo "127.0.0.1 localhost $(hostname)" > /etc/hosts && \  
./scripts/setup/install && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80 443  
CMD ["tail", "-f", "/dev/null"]  
  


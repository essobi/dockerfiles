FROM gliderlabs/alpine:3.4  
  
ADD config /config  
  
RUN apk-install -t my-tools wget unzip gnupg curl && \  
apk-install ca-certificates && \  
cd /tmp && \  
wget https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_SHA256SUMS.sig
&& \  
wget https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_SHA256SUMS && \  
wget https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_linux_amd64.zip
&& \  
curl https://keybase.io/hashicorp/key.asc | gpg --import && \  
gpg --verify consul_0.6.4_SHA256SUMS.sig consul_0.6.4_SHA256SUMS && \  
grep consul_0.6.4_linux_amd64.zip consul_0.6.4_SHA256SUMS | sha256sum -c && \  
unzip consul_0.6.4_linux_amd64.zip -d /usr/local/bin && \  
mkdir /data && \  
apk del my-tools && \  
rm -rf /tmp/*  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
ENTRYPOINT ["/usr/local/bin/consul", "agent", "-config-dir=/config"]  


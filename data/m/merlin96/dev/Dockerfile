FROM debian:8.7  
# Install basics for work with docker and rancher  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -yqq install \  
net-tools \  
docker.io \  
mc \  
nano \  
openssh-server \  
curl \  
wget  
  
# Use UTF-8 and not POSIX for frames in mc  
RUN echo "export LANG=\"C.UTF-8\"" >> /root/.bashrc  
  
# Install rancher cli  
RUN wget -qO- https://github.com/rancher/cli/releases/download/v0.4.1/rancher-
linux-amd64-v0.4.1.tar.gz | tar xvz -C /tmp && \  
mv /tmp/rancher-v0.4.1/rancher /usr/local/bin/rancher && \  
chmod +x /usr/local/bin/rancher  
  
# Install docker compose cli  
RUN curl -L "https://github.com/docker/compose/releases/download/1.9.0/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
# Install azure cli  
RUN mv /bin/sh /bin/sh.backup && ln -s /bin/bash /bin/sh  
ENV AZURE_CLI_VERSION "0.10.9"  
ENV NODEJS_APT_ROOT "node_4.x"  
ENV NODEJS_VERSION "4.7.0"  
RUN apt-get install -qqy --no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
git \  
lsb-release \  
python-all \  
rlwrap \  
jq && \  
rm -rf /var/lib/apt/lists/* && \  
curl
https://deb.nodesource.com/${NODEJS_APT_ROOT}/pool/main/n/nodejs/nodejs_${NODEJS_VERSION}-1nodesource1~jessie1_amd64.deb
> node.deb && \  
dpkg -i node.deb && \  
rm node.deb && \  
npm install --global azure-cli@${AZURE_CLI_VERSION} && \  
azure --completion >> ~/azure.completion.sh && \  
echo 'source ~/azure.completion.sh' >> ~/.bashrc && \  
azure  
  
# ssh stuff  
RUN mkdir /var/run/sshd && \  
echo 'root:secretpw' | chpasswd && \  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config &&
\  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
VOLUME /var/run/docker.sock /root  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  


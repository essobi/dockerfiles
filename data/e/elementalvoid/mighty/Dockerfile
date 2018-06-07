FROM debian:jessie  
MAINTAINER Matt Klich <matt@elementalvoid.com>  
  
RUN sed -i -e 's/main$/main contrib non-free/' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
bash-completion \  
ca-certificates \  
curl \  
file \  
less \  
openssh-client \  
rsync \  
unzip \  
wget && \  
apt-get install -y \  
build-essential \  
git \  
python \  
python-setuptools \  
tmux \  
ruby \  
vim-nox && \  
easy_install pip && \  
apt-get clean  
  
WORKDIR /root  
ENV IN_CONTAINER=true  
ENV SSH_AUTH_SOCK /ssh-auth-sock  
  
RUN curl -sL git.io/evoid-install > /tmp/evoid-install.sh && \  
bash /tmp/evoid-install.sh  
  
CMD ["/bin/bash"]  


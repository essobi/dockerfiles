FROM ubuntu:14.04  
MAINTAINER Tom George  
  
# ENV http_proxy http://10.0.2.2:3128  
# ENV https_proxy https://10.0.2.2:3128  
ENV GO_VERSION 1.9.3.linux-amd64  
ENV KUBECTL_VERSION 1.9.0  
ENV ISTIO_VERSION 0.5.1  
ARG DOCKER_GID  
  
# ADD 01proxy /etc/apt/apt.conf.d  
RUN apt-get update && \  
apt-get install -y vim \  
software-properties-common \  
wget \  
curl \  
libcurl4-openssl-dev \  
zsh \  
dos2unix \  
tmux \  
build-essential \  
git \  
apt-file \  
python3-pip \  
apt-transport-https \  
ca-certificates \  
man \  
unzip \  
ctags  
  
RUN rm /etc/localtime && \  
ln -s /usr/share/zoneinfo/America/New_York /etc/localtime && \  
locale-gen en_US.UTF-8  
  
ADD https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64
/usr/local/bin/gosu  
RUN chmod 775 /usr/local/bin/gosu  
  
RUN curl -L
https://github.com/docker/compose/releases/download/1.19.0-rc2/docker-
compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
ADD https://dl.google.com/go/go$GO_VERSION.tar.gz /usr/local  
RUN cd /usr/local && \  
tar -xvf go$GO_VERSION.tar.gz && \  
rm go$GO_VERSION.tar.gz && \  
mkdir -p /home/dev/go \  
/home/dev/bin \  
/home/dev/lib \  
/home/dev/include \  
/var/shared && \  
touch /var/shared/placeholder && \  
ln -s /var/shared/.ssh  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add
-  
  
RUN groupadd -g $DOCKER_GID docker  
RUN add-apt-repository ppa:neovim-ppa/unstable && \  
add-apt-repository ppa:ansible/ansible && \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
\  
$(lsb_release -cs) \  
stable" && \  
apt-get update && \  
apt-get install -y docker-ce neovim ansible && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH /home/dev/bin:/usr/local/go/bin:$PATH  
ENV LD_LIBRARY_PATH /home/dev/lib:$LD_LIBRARY_PATH  
  
VOLUME /var/shared  
  
WORKDIR /home/dev  
ENV HOME /home/dev  
RUN mkdir -p /home/dev/.local/share/nvim/shada && \  
touch /home/dev/.local/share/nvim/shada/main.shada && \  
chmod -R 775 /home/dev/.local  
  
RUN git clone https://github.com/tomgeorge/oh-my-zsh.git ~/.oh-my-zsh && \  
git clone https://github.com/tomgeorge/dotfiles && \  
git clone https://github.com/tomgeorge/vimfiles /home/dev/.vim && \  
cd dotfiles && \  
./links.sh  
  
RUN pip3 install neovim awscli && \  
nvim -E -s -c "source ~/.config/nvim/init.vim" -c PluginInstall -c qa -V ||
true && \  
nvim -E -s -c "source ~/.config/nvim/init.vim" -c UpdateRemotePlugins -c qa -V
|| true  
  
ADD docker_entrypoint.sh /usr/local/bin  
RUN chmod 775 /usr/local/bin/docker_entrypoint.sh  
  
RUN wget
https://releases.hashicorp.com/terraform/0.11.2/terraform_0.11.2_linux_amd64.zip?_ga=2.104669568.1844800320.1517421482-308538760.1517421482
&& unzip
terraform_0.11.2_linux_amd64.zip?_ga=2.104669568.1844800320.1517421482-308538760.1517421482
-d /usr/local/bin && rm
terraform_0.11.2_linux_amd64.zip?_ga=2.104669568.1844800320.1517421482-308538760.1517421482  
  
RUN wget https://storage.googleapis.com/kubernetes-
release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl && \  
chmod +x kubectl && \  
mv kubectl /usr/local/bin  
  
RUN wget
https://github.com/istio/istio/releases/download/0.5.1/istio-$ISTIO_VERSION-
linux.tar.gz && \  
tar -xvf istio-$ISTIO_VERSION-linux.tar.gz && \  
mv istio-$ISTIO_VERSION/bin/istioctl /usr/local/bin && \  
chmod +x /usr/local/bin/istioctl && \  
rm -rf istio-$ISTIO_VERSION  
  
ENTRYPOINT ["docker_entrypoint.sh"]  
CMD ["/usr/bin/zsh"]  


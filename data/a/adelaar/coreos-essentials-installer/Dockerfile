# Copyright 2017 Jacek Kurasiewicz  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
  
############################################################  
# Maitained by Jacek Kurasiewicz  
# Email: jk (at) adelaartech (dot) com  
#  
# Dockerfile to build OhMyZsh container images  
# Based on the latest Ubuntu Server  
############################################################  
  
# Set the base image to Ubuntu Server  
FROM ubuntu:latest  
  
# File Author / Maintainer  
MAINTAINER Jacek Kurasiewicz  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV HOME=/root  
ENV PATH="/root/bin:${PATH}"  
ENV TZ=America/New_York  
ENV DOCKERCOMPOSE_VERSION=1.14.0  
  
COPY bin /root/bin  
  
#RUN /opt/bin/apt-proxy-setup.sh  
#RUN echo 'Acquire::http { Proxy "http://192.168.1.111:3142/"; };' >>
/etc/apt/apt.conf.d/01proxy && \  
  
# Upgrade Ubuntu  
RUN apt-get update && \  
apt-get upgrade -y && \  
  
# Install needed packages  
apt-get install -y zsh zsh-common git git-core tmux nano mc sed curl wget \  
sudo net-tools inetutils-ping bash-completion mc tmux openssh-client vim \  
gcc make autoconf yodl libncursesw5-dev texinfo checkinstall tzdata && \  
  
# Install docker-compose  
curl -L
https://github.com/docker/compose/releases/download/${DOCKERCOMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose && \  
  
# Install oh-my-zsh for ROOT user  
wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O
- | zsh || true && \  
sed -i -E "s/^ZSH_THEME=\"robbyrussell\"/ZSH_THEME=\"softpro\"/" /root/.zshrc
&& \  
sed -i -E "s/^plugins=\\((.*)\\)$/plugins=(\1 tmux docker docker-compose)/"
/root/.zshrc && \  
sed -i "3iexport PATH=/root/bin:/usr/local/bin:$PATH" /root/.zshrc && \  
# Remove last-working-directory plugin && \  
rm -R ~/.oh-my-zsh/plugins/last-working-dir && \  
  
apt-get clean && \  
rm -rf /var/lib/apt  
  
#RUN rm /etc/apt/apt.conf.d/01proxy 2> /dev/null  
  
ENV DEBIAN_FRONTEND=teletype  
  
COPY files/softpro.zsh-theme /root/.oh-my-zsh/themes/softpro.zsh-theme  
  
WORKDIR /root  
  
CMD ["/bin/bash"]


FROM ubuntu  
MAINTAINER Herman Junge "chpdg42@gmail.com"  
  
###############################################################################  
#  
# APT packages  
#  
# * curl  
# * git  
# * vim-gnome: Support for python, which is not enabled by default  
# * build-essential: Compile your own stuff  
# * locales: Fix that infamous problem  
#  
###############################################################################  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
git \  
vim-gnome \  
build-essential \  
locales && \  
locale-gen en_US.UTF-8 && \  
apt-get upgrade -y  
  
###############################################################################  
#  
# Docker  
#  
# Latest docker client  
#  
###############################################################################  
  
RUN curl -o /tmp/docker-latest.tgz \  
https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz && \  
tar xfvz /tmp/docker-latest.tgz -C /tmp/ && \  
mv /tmp/docker/docker /usr/bin/docker && \  
rm -rf /tmp/docker /tmp/docker-latest.tgz && \  
chmod +x /usr/bin/docker  
  
###############################################################################  
#  
# go + goimports (golang 1.9.2)  
#  
###############################################################################  
  
RUN curl -o /tmp/go1.9.2.linux-amd64.tar.gz \  
https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz && \  
tar -xvf /tmp/go1.9.2.linux-amd64.tar.gz -C /tmp/ && \  
GOROOT=/tmp/go GOPATH=/tmp/gopath \  
/tmp/go/bin/go get golang.org/x/tools/cmd/goimports && \  
mv /tmp/go /usr/local && \  
mv /tmp/gopath/ /go && \  
rm -rf /tmp/go1.9.2.linux-amd64.tar.gz  
  
###############################################################################  
#  
# VIM  
#  
# A fork from scrooloose + vim-go + some extra configs  
#  
###############################################################################  
  
RUN git clone https://github.com/hermanjunge/vimfiles.git /root/.vim && \  
cd /root/.vim && \  
git submodule init && \  
git submodule update && \  
ln -s /root/.vim/vimrc /root/.vimrc  
  
###############################################################################  
#  
# Bash Stuff  
#  
# * .bashrc  
# * git-completion  
#  
###############################################################################  
  
ADD bashrc /root/.bashrc  
RUN curl \  
https://raw.githubusercontent.com/git/git/master/contrib/completion/git-
completion.bash \  
-o \  
/root/.git-completion.bash  
  
###############################################################################  
#  
# We are set  
#  
###############################################################################  
  
WORKDIR /root  


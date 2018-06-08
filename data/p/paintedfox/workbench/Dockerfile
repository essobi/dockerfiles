# My Docker Workbench.  
# The workbench is for linking to a running docker container that exposes ssh.  
# Workbench containers are meant to be disposable and not long lived.  
FROM ubuntu  
MAINTAINER Ryan Seto <ryanseto@yak.net>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade  
  
# Ensure UTF-8  
RUN apt-get update  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install all the tools that I need.  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get install -y python-software-properties && \  
add-apt-repository -y ppa:keithw/mosh && \  
apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl wget aria2 rsync \  
git bzr mercurial \  
zip p7zip-full bzip2 \  
ssh mosh \  
tcl python python-setuptools \  
tmux vim-nox diffutils patch  
  
ENV HOME /root  
  
RUN git clone https://github.com/Painted-Fox/dotfiles $HOME/dotfiles  
RUN tclsh $HOME/dotfiles/update.tcl  
RUN $HOME/dotfiles/setup-linux.sh  
  
ENTRYPOINT ["bash", "-il"]  


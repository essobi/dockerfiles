FROM ubuntu:18.04  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# update and install minimal os and various utilities  
RUN apt-get update &&\  
apt-get -y dist-upgrade &&\  
DEBIAN_FRONTEND=noninteractive apt-get -y install ubuntu-minimal ubuntu-
standard \  
software-properties-common wget curl zsh tree xdot  
  
# add PPAs  
RUN add-apt-repository ppa:neovim-ppa/unstable &&\  
apt-get update  
  
# install essential build tools  
RUN apt-get -y install git build-essential clang autoconf pkg-config  
  
# install neovim  
RUN apt-get -y install \  
neovim python-dev python-pip python3-dev python3-pip xclip &&\  
pip2 install -U neovim &&\  
pip3 install -U neovim &&\  
update-alternatives --install /usr/bin/vi vi /usr/bin/nvim 60 &&\  
update-alternatives --install /usr/bin/vim vim /usr/bin/nvim 60 &&\  
update-alternatives --install /usr/bin/editor editor /usr/bin/nvim 60  
  
# clean apt-get  
RUN apt-get autoremove --purge &&\  
apt-get clean  
  
# add user  
ENV USER=george  
RUN useradd -k /mnt -Ums /bin/zsh $USER &&\  
echo "$USER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-$USER  
USER $USER  
WORKDIR /home/$USER  
# setup home  
ADD . /tmp/home  
RUN sudo chown -R $USER:$USER /tmp/home && /tmp/home/setup && rm -rf /tmp/home  
  
ENV PATH=$PATH:/home/$USER/bin  
  
CMD /bin/zsh  


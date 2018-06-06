FROM debian:stable  
  
RUN \  
apt-get update && \  
apt-get install -y man git vim-nox \  
screen wget curl xz-utils ncdu pax-utils unzip zip \  
sysstat fio gnuplot graphicsmagick-imagemagick-compat blktrace hdparm lshw
hwinfo &&\  
rm -rf /var/lib/apt/lists/* &&\  
apt-get clean -yq  
  
RUN cd ~ &&\  
git clone https://github.com/chin33z/fio_baseline.git  
  
# 1. git clone the vim setting  
# 2. git clone the env setting  
RUN \  
rm -fr ~/.vim ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/dotvim.git ~/.vim &&\  
ln -s ~/.vim/vimrc ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/dotfiles.git ~/dotfiles &&\  
cd dotfiles && ./link.sh  
  
ENV HOME /root  
WORKDIR /root  


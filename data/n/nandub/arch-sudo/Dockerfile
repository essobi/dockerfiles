# BUILD-USING: docker build -t nandub/arch-sudo .  
# TEST-USING: docker run --rm -i -t -h=arch-sudo --name=arch-sudo nandub/arch-
sudo /bin/bash  
# RUN-USING: docker run --rm -h=arch-sudo --name=arch-sudo nandub/arch-sudo  
#An arch environment to only allow sudo for running commands  
#VERSION 0.0.1  
FROM base/archlinux  
MAINTAINER Fernando Ortiz <dev+docker@nandub.info>  
  
# Update the repositories  
RUN pacman -Syy  
  
# Install sudo libunistring gcc binutils make  
RUN pacman -S --noconfirm sudo \  
libunistring \  
gcc \  
binutils \  
make  
  
RUN groupadd -r docker  
RUN useradd -m docker -g docker -s /bin/bash && echo '%docker ALL=(ALL)
NOPASSWD:ALL' >> /etc/sudoers  
  
USER docker  


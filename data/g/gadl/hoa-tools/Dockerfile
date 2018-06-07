FROM debian:sid  
MAINTAINER Alexandre Duret-Lutz <adl@lrde.epita.fr>  
RUN apt-get update && \  
RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y \  
wget vim-nox emacs-nox \  
openjdk-8-jre-headless \  
gcc-4.9 \  
g++-4.9 \  
make \  
libbdd0c2 \  
libbdd-dev \  
graphviz && \  
apt-get clean && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 20 && \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 20  
  
COPY install.sh /tmp/install.sh  
RUN cd /tmp && ./install.sh && rm -f install.sh  
  
RUN mkdir -p /home/user && groupadd -r user && useradd -r -g user user &&
chown user:user /home/user  
WORKDIR /home/user  
COPY README /home/user/README  
USER user  


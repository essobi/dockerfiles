FROM ubuntu:16.04  
MAINTAINER André Bauer <andre.bauer@posteo.de>  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
aspcud \  
ca-certificates \  
wget \  
git \  
mercurial \  
darcs \  
sudo \  
make \  
unzip \  
rsync \  
m4 \  
build-essential \  
curl \  
openssh-client && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
RUN wget https://raw.github.com/ocaml/opam/master/shell/opam_installer.sh -O -
| sh -s /usr/local/bin  
RUN echo 'ocaml ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/ocaml && \  
chmod 440 /etc/sudoers.d/ocaml && \  
chown root:root /etc/sudoers.d/ocaml && \  
useradd -d /home/ocaml -m -s /bin/bash ocaml -G sudo && \  
passwd -l ocaml && \  
chown -R ocaml:ocaml /home/ocaml  
USER ocaml  
ENV HOME /home/ocaml  
WORKDIR /home/ocaml  
RUN opam init --comp 4.04.0 && \  
eval `opam config env` && \  
opam update && \  
opam install depext  
RUN . /home/ocaml/.opam/opam-init/init.sh > /dev/null 2> /dev/null || true  
RUN echo "eval \\`opam config env\\`" >> /home/ocaml/.bashrc


FROM ubuntu:14.04  
LABEL ruby.version="2.2" exonerate.version="2.2.0" glib.version="2.31.12"
mafft.version="7.123b" primer3.version="2.3.6"  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER root  
  
RUN apt-get -y update && apt-get -yy install apt-utils autoconf automake bison
build-essential bzip2 curl exonerate g++ gawk gawk-doc gcc git-core libbz2-dev
libffi-dev libgdbm-dev libgmp10-doc libgmpxx4ldbl liblzma-dev libmpfr-dev
libncurses5-dev libpq-dev libreadline6 libreadline6-dev libreadline-dev
libsqlite3-dev libssl-dev libtool libyaml-dev mafft make ncbi-blast+ openbox
openssl patch pkg-config primer3 python-software-properties ruby-dev ruby-full
sqlite sqlite3-doc wget xorg zlib1g-dev  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable  
RUN echo source /etc/profile.d/rvm.sh >> /.bashrc  
RUN /bin/bash -c "source /.bashrc; rvm install 2.2; rvm use 2.2 --default;gem
install bio-polyploid-tools"  
  
WORKDIR /data/  
  


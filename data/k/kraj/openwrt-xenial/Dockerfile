# Pull base image.  
FROM ubuntu:16.04  
  
MAINTAINER Khem Raj <raj.khem@gmail.com>  
  
# Install.  
RUN apt-get update && \  
apt-get install -yq sudo build-essential \  
gradle \  
mtd-utils \  
python-jenkins \  
python-pexpect \  
python-tabulate \  
python-termcolor \  
python3-paramiko \  
autopoint \  
libncurses5-dev \  
subversion \  
zlib1g-dev \  
doxygen doxygen-latex texlive-base texlive-fonts-recommended \  
zip unzip \  
gettext \  
libssl-dev \  
python-pip python-lxml \  
libxml2-utils \  
libbsd-dev \  
libpcap-dev \  
ocaml-nox \  
openvswitch-common openvswitch-switch \  
autoconf \  
bison \  
flex \  
locales \  
libacl1-dev \  
libtool \  
curl \  
gawk \  
wget \  
gnutls-dev \  
libcurl4-openssl-dev \  
libjson-c-dev \  
patchutils \  
sharutils \  
tcsh \  
git vim \  
u-boot-tools \  
device-tree-compiler \  
libmosquitto1 \  
libmosquitto-dev \  
libprotobuf-c1 \  
libprotobuf-c-dev \  
libev4 \  
libev-dev \  
libjansson4 \  
libjansson-dev \  
protobuf-c-compiler && \  
rm -rf /var/lib/apt-lists/* && \  
echo "dash dash/sh boolean false" | debconf-set-selections && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash  
  
# clean up  
RUN apt-get -y clean  
  
# Install Google's "repo" tool and make it executable  
RUN curl http://storage.googleapis.com/git-repo-downloads/repo >
/usr/local/bin/repo  
RUN chmod +x /usr/local/bin/repo  
  
RUN useradd -ms /bin/bash -p build build && \  
usermod -aG sudo build  
# give users in the sudo group sudo access in the container  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
COPY ./bashrc /home/build/.bashrc  
  
# Set environment variables.  
ENV LANG en_US.utf8  
ENV TIGRESS_HOME /home/build/tigress-2.2  
ENV PATH /home/build/tigress-2.2:$PATH  
  
USER build  
  
# Define working directory.  
WORKDIR /home/build  
  
RUN curl -O https://uclibc.org/~kraj/tigress-Linux-x86_64-2.2.zip && \  
unzip tigress-Linux-x86_64-2.2.zip -d /home/build  
  
# Define default command.  
CMD ["bash"]  
  


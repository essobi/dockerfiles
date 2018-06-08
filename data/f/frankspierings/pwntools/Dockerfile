FROM ubuntu:latest  
MAINTAINER Frank Spierings  
  
# Base setup  
RUN dpkg --add-architecture i386 && \  
apt-get update && apt-get upgrade -y && \  
apt-get install libstdc++6:i386 -y  
  
# Locales setup  
RUN apt-get install locales -y && locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Convenience setup  
RUN apt-get install python python-pip bsdmainutils qemu strace ltrace vim tmux
-y && \  
pip install --upgrade pip && \  
pip install --upgrade ipython  
  
# GDB setup  
RUN apt-get install gdbserver gdb-multiarch -y  
  
# Pwndbg  
RUN apt-get install sudo git -y && \  
pip install --upgrade git+https://github.com/sashs/ropper.git && \  
DSTDIR=/opt && \  
cd ${DSTDIR} && \  
git clone https://github.com/pwndbg/pwndbg && \  
cd pwndbg && ./setup.sh  
  
# Peda (default disabled)  
RUN DSTDIR=/opt && \  
apt-get install nasm -y && \  
git clone https://github.com/longld/peda.git ${DSTDIR}/peda && echo "# source
${DSTDIR}/peda/peda.py" >> ~/.gdbinit  
  
# Gef (default disabled)  
RUN DSTDIR=/opt && \  
apt-get install cmake wget -y && \  
pip3 install --upgrade keystone-engine && \  
mkdir -p ${DSTDIR}/gef && \  
wget -O "${DSTDIR}/gef/gdbinit-gef.py" -q
"https://github.com/hugsy/gef/raw/master/gef.py" && \  
echo "# source ${DSTDIR}/gef/gdbinit-gef.py" >> ~/.gdbinit  
  
# Pwntools  
RUN apt-get install libcapstone3 python2.7 python-pip python-dev git libssl-
dev libffi-dev build-essential -y && \  
pip install --upgrade pip && \  
pip install --upgrade git+https://github.com/Gallopsled/pwntools.git  
  
# Angr for symbolic execution  
RUN pip install --upgrade angr  
  
# Clean up  
RUN apt-get autoclean -y && \  
apt-get autoremove -y && rm -rf /tmp/*  
  
###  
### Build this file: `docker build -t pwntools .`  
### Run (iTerm2): `docker run -it -v /tmp/data:/tmp/data --privileged --name
pwntools --hostname pwntools pwntools tmux -CC`  
###


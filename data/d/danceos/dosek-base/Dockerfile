FROM ubuntu:trusty  
MAINTAINER Christian Dietrich <stettberger@dokucode.de>  
  
RUN apt-get update; apt-get install -y \  
binutils-dev \  
build-essential \  
clang-3.4 \  
cmake \  
g++-multilib \  
gcc-multilib \  
git \  
grub-common \  
grub-pc-bin \  
llvm-3.3-dev \  
llvm-3.3-runtime \  
openssh-server \  
python-minimal \  
python3 \  
python3-lxml \  
python3-pip \  
python3-pyparsing \  
qemu-system-x86 \  
screen \  
vim \  
xorriso  
  
# Unfortunately we have to install python-llvm from the PiP  
RUN LLVM_CONFIG_PATH=/usr/bin/llvm-config-3.3 pip3 install llvmpy  
  
RUN useradd dosek; \  
mkdir /home/dosek; \  
chown dosek /home/dosek; \  
echo 'dosek:dosek' | chpasswd; \  
chsh dosek --shell /bin/bash; \  
adduser dosek sudo  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN mkdir /var/run/sshd; \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
USER dosek  
ENV HOME /home/dosek  
WORKDIR /home/dosek  
  
RUN git clone https://github.com/danceos/dosek.git  
WORKDIR dosek  
  
# Run the Testsuite  
RUN mkdir build; cd build; ../new_build_env.py; \  
make -j$(getconf _NPROCESSORS_ONLN) ctest2jenkins; \  
cd ..; rm -rf build  
  
# Start the SSH Server  
USER root  
EXPOSE 22  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
CMD ["/usr/sbin/sshd", "-D"]  
  


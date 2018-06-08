FROM ubuntu:14.04.3  
MAINTAINER sjkim.pgm@gmail.com  
  
# Change timezone  
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime \  
# Set local  
&& locale-gen en_US.UTF-8 \  
  
&& apt-get update \  
&& apt-get install -y \  
software-properties-common \  
wget \  
sudo \  
## Add repository for llvm/clang 3.8  
# && wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key|sudo apt-key add - \  
# && add-apt-repository "deb http://llvm.org/apt/trusty/ llvm-toolchain-
xenial-3.8 main" \  
# Add repository for fish  
&& apt-add-repository ppa:fish-shell/release-2 \  
# Add repository for neovim  
&& add-apt-repository ppa:neovim-ppa/unstable \  
# Install necessary tools  
&& apt-get update \  
&& apt-get install -y \  
apt-transport-https \  
# clang-3.8 \  
cmake \  
curl \  
fish \  
default-jdk \  
gdb \  
git \  
g++ \  
man-db \  
neovim \  
openssh-server \  
python-dev \  
python-pip \  
screen \  
sysstat \  
tmux \  
vim \  
## Clang config  
# && update-alternatives --install /usr/bin/llvm-config llvm-config
/usr/bin/llvm-config-3.8 10 \  
# && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.8 10
\  
# neovim config  
&& update-alternatives --install /usr/bin/vim vim /usr/bin/nvim 10 \  
&& update-alternatives --set vim /usr/bin/nvim \  
&& pip install neovim \  
# Add sjkim user  
&& useradd -m -u 12345 -d /home/sjkim/ sjkim \  
&& chsh -s /usr/bin/fish sjkim \  
&& echo "sjkim:$(openssl rand -base64 20)" | chpasswd \  
&& echo "sjkim ALL=NOPASSWD: ALL" > /etc/sudoers.d/sjkim \  
# Run SSH server  
&& mkdir /var/run/sshd \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Ports  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D", "-E", "/var/log/sshd"]  


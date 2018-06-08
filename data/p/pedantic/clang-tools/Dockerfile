FROM debian:sid-slim  
ENV VER=7  
RUN apt-get update && \  
apt-get install -y \  
clang-${VER} \  
clang-${VER}-doc \  
clang-format-${VER} \  
clang-tidy-${VER} \  
clang-tools-${VER} \  
llvm-${VER}-tools \  
lldb-${VER} \  
vim \  
zsh \  
cmake \  
sudo \  
less \  
wget \  
curl \  
git  
  
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-${VER}
100 \  
\--slave /usr/bin/clang++ clang++ /usr/bin/clang++-${VER} \  
\--slave /usr/bin/clang-format clang-format /usr/bin/clang-format-${VER} \  
\--slave /usr/bin/clang-tidy clang-tidy /usr/bin/clang-tidy-${VER}  
  
RUN adduser --uid 1000 -gid 100 --disabled-password --disabled-login --gecos
"" clang && \  
usermod -a -G sudo clang && \  
sed -i '/^\%sudo/c%sudo ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers  
  
WORKDIR /home/clang  
USER 1000:100  


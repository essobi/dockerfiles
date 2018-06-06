FROM buildpack-deps:xenial  
  
# Install a number of usefull tools  
# Create user "builder" with password "builder"  
# Allow passwordless sudo for "builder" user  
RUN set -ex; \  
apt-get update && apt-get install -y vim htop tree tmux sudo bash-completion
&& \  
useradd builder -m -s /bin/bash && echo "builder:builder" | chpasswd && \  
echo "builder ALL = (ALL) NOPASSWD: ALL" > /etc/sudoers.d/builder;  
  
# Switch to "builder" user  
USER builder  
WORKDIR /home/builder/  
  
# Clone depot-tools repo and add it to PATH  
RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git  
ENV PATH="$PATH:/home/builder/depot_tools"  
# Clone chromium repo  
RUN set -ex; \  
mkdir chromium && cd chromium && \  
fetch --nohooks chromium  
  
WORKDIR /home/builder/chromium/src  


FROM ubuntu:xenial  
  
LABEL maintainer "https://github.com/blacktop"  
  
# ENV TERM screen-256color  
ENV TERM xterm-256color  
ENV GDB_VERSION 7.11.1-0ubuntu1~16.5  
RUN buildDeps='ca-certificates git build-essential wget python3-pip
python3-dev libreadline6-dev pkg-config' \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -yq $buildDeps \  
sudo \  
tmux \  
ltrace \  
strace \  
python3 \  
ruby2.3 \  
locales \  
binutils \  
libc6:i386 \  
python3-yaml \  
libstdc++6:i386 \  
gdb=$GDB_VERSION \  
gdb-multiarch=$GDB_VERSION \  
&& echo "===> Fix locale..." \  
&& locale-gen en_US.UTF-8 \  
&& localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& echo "===> Install voltron..." \  
&& export PIP_NO_CACHE_DIR=off \  
&& export PIP_DISABLE_PIP_VERSION_CHECK=on \  
&& pip3 install --upgrade pip wheel setuptools capstone \  
&& cd /tmp \  
&& git clone https://github.com/snare/voltron \  
&& cd voltron \  
&& ./install.sh -S -b gdb \  
&& echo "===> Clean up unnecessary files..." \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get install -y tmuxinator \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
ENV PATH /root/.local/bin:$PATH  
  
COPY voltron/tmuxinator/voltron.yml /root/.tmuxinator/voltron.yml  
  
WORKDIR samples  
  
ENTRYPOINT ["tmuxinator","start","voltron"]  


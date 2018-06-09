FROM ubuntu:16.04  
  
ENV SHELL bash  
  
RUN apt-get update && apt-get install -y \  
bash-completion \  
build-essential \  
exuberant-ctags \  
git \  
python-pip-whl \  
python2.7 \  
python2.7-dev \  
python2.7-setuptools \  
python3 \  
python3-dev \  
python3-pip \  
python3-setuptools \  
python3-wheel \  
perl \  
screen \  
software-properties-common \  
tmux \  
vim \  
\  
curl \  
dnsutils \  
dstat \  
iftop \  
htop \  
iputils-ping \  
jq \  
netcat \  
net-tools \  
tcpdump \  
telnet \  
wget \  
whois \  
&& add-apt-repository ppa:neovim-ppa/unstable \  
&& apt-get update \  
&& apt-get install -y neovim \  
&& easy_install pip \  
&& pip install neovim \  
&& pip3 install neovim \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd ubuntu \  
&& curl -L https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 >
/usr/local/bin/gosu \  
&& curl -L https://github.com/tianon/gosu/releases/download/1.10/gosu-
amd64.asc > /usr/local/bin/gosu.asc \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& chmod +sx /usr/local/bin/gosu \  
&& rm /usr/local/bin/gosu.asc  
  
COPY . /home/ubuntu/dotfiles  
  
RUN chown -R ubuntu:ubuntu /home/ubuntu  
  
USER ubuntu  
  
WORKDIR /home/ubuntu  
  
RUN ( \  
cd dotfiles; \  
./install.sh; \  
/usr/bin/vim -S vim-plug-snapshot.vim +qall; \  
nvim -S nvim-plug-snapshot.vim +qall \  
)  


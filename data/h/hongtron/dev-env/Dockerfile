FROM debian:stretch  
  
# Locales  
ENV LANG=en_US.UTF-8  
RUN apt-get update && apt-get install -y locales  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen  
RUN locale-gen en_US.UTF-8  
  
# Colors and italics for tmux  
COPY xterm-256color-italic.terminfo /root  
RUN tic /root/xterm-256color-italic.terminfo  
ENV TERM=xterm-256color-italic  
  
# Common packages  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
htop \  
iputils-ping \  
jq \  
libncurses5-dev \  
libevent-dev \  
net-tools \  
netcat-openbsd \  
rubygems \  
ruby-dev \  
tmux \  
openjdk-8-jre \  
tzdata \  
wget \  
vim \  
zsh  
  
RUN chsh -s /usr/bin/zsh  
  
# Install tmux  
WORKDIR /usr/local/src  
RUN wget https://github.com/tmux/tmux/releases/download/2.5/tmux-2.5.tar.gz  
RUN tar xzvf tmux-2.5.tar.gz  
WORKDIR /usr/local/src/tmux-2.5  
RUN ./configure  
RUN make  
RUN make install  
RUN rm -rf /usr/local/src/tmux*  
  
# Install neovim v0.2.2  
RUN apt-get install -y \  
autoconf \  
automake \  
cmake \  
g++ \  
libtool \  
libtool-bin \  
pkg-config \  
python3 \  
python3-pip \  
unzip  
RUN pip3 install --upgrade pip &&\  
pip3 install --user neovim jedi mistune psutil setproctitle  
WORKDIR /usr/local/src  
RUN git clone \--depth 1 https://github.com/neovim/neovim.git  
WORKDIR /usr/local/src/neovim  
RUN git fetch --depth 1 origin tag v0.2.2  
RUN git reset --hard v0.2.2  
RUN make CMAKE_BUILD_TYPE=Release  
RUN make install  
RUN rm -rf /usr/local/src/neovim  
  
# Install rvm  
RUN echo 'export rvm_prefix="$HOME"' > /root/.rvmrc  
RUN echo 'export rvm_path="$HOME/.rvm"' >> /root/.rvmrc  
RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import -  
RUN curl -sSL https://get.rvm.io | bash -s stable --rails  
  
# Misc ruby  
RUN /bin/bash -c "source /root/.rvm/scripts/rvm && gem install bundler pry
pry-byebug pry-rescue neovim"  
  
# Install docker  
WORKDIR /usr/local/src  
RUN curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh  
RUN rm /usr/local/src/get-docker.sh  
  
# Install elixir  
WORKDIR /usr/local/src  
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb &&
dpkg -i erlang-solutions_1.0_all.deb && apt-get update  
RUN apt-get install -y esl-erlang  
RUN apt-get install -y elixir  
RUN rm erlang-solutions_1.0_all.deb  
  
# Install docker-compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && chmod +x
/usr/local/bin/docker-compose  
  
# Configure git  
RUN echo "[user]\n name = hongtron\n email = me@aliho.ng" >> /root/.gitconfig  
  
# Dotfiles 😎  
COPY dotfiles /root/dotfiles  
WORKDIR /root/dotfiles  
RUN rake install  
  
WORKDIR /root  
CMD /bin/bash -i -c "tmux-start ali"  


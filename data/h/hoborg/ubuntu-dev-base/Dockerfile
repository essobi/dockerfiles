FROM ubuntu:xenial  
# pass in when building the image  
ARG PROXY=''  
# Proxies  
ENV http_proxy=$PROXY  
ENV https_proxy=$PROXY  
  
ENV TERM screen-256color  
  
ENV USER devbox  
ENV HOME /home/$USER  
ENV XDG_CONFIG_HOME $HOME/.config  
WORKDIR /home/$USER  
  
# Disable http cache and pipeline, fixes some download bugs  
RUN echo 'Acquire::http::No-Cache true;\nAcquire::http::Pipeline-Depth 0;' \  
>> /etc/apt/apt.conf.d/no-pipeline  
  
# A lot of this was copied from AGhost-7/docker-dev  
RUN apt-get update && \  
apt-get install sudo locales -y && \  
adduser --disabled-password --gecos '' $USER && \  
adduser $USER sudo && \  
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
# Locale (unicode characters broken if not set!!!)  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Add PPA repositories  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends software-properties-common  
RUN add-apt-repository ppa:git-core/ppa  
RUN add-apt-repository ppa:neovim-ppa/stable  
  
# Update package list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install from standard repos  
RUN apt-get install -y --no-install-recommends mc bash zsh automake pkg-config
libpcre3-dev \  
tmux rubygems build-essential make tree curl man-db sudo software-properties-
common \  
zlib1g-dev liblzma-dev libssl-dev xsel ctags \  
python libpython2.7-dev python-setuptools python-pip \  
python3 libpython3.5-dev python3-setuptools python3-pip  
  
# Install from PPAs  
RUN apt-get install -y git neovim  
  
# Install neovim and trash-cli for python (requried by neovim and rmtrash)  
RUN pip install -U pip  
RUN pip install neovim  
RUN pip3 install -U pip  
RUN pip3 install neovim virtualenvwrapper trash-cli  
  
# Install homesick and 'rouge' ruby highlighter  
RUN gem install homesick rouge  
  
# For some reason the user folder is not owned by the user  
RUN chown -R "$USER":"$USER" /home/$USER  
  
# Change shell to zsh  
RUN chsh -s /usr/bin/zsh  
RUN chsh -s /usr/bin/zsh $USER  
  
# User-specific part follows  
USER $USER  
# Install pyenv  
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv  
RUN git clone https://github.com/pyenv/pyenv-virtualenv.git
~/.pyenv/plugins/pyenv-virtualenv  
  
# Run build script for homesick etc.  
COPY ./build.sh /tmp/build.sh  
RUN bash /tmp/build.sh && sudo rm /tmp/build.sh  
  
# Reset shell (it is usually garbled by nvim)  
RUN tput reset  
  
CMD ["/usr/bin/zsh"]  


FROM ubuntu:16.04  
  
RUN apt-get update && \  
# Neovim:  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:neovim-ppa/unstable && \  
apt-get update && \  
apt-get install -y \  
neovim \  
python-dev \  
python-pip \  
python3-dev \  
python3-pip \  
  
# Miscellaneous:  
curl \  
git \  
mercurial \  
postgresql-client \  
  
# Enable Neovim's Python3 interface:  
&& pip3 install neovim \  
  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
#################################################  
# Workspace Setup  
#################################################  
  
ENV TZ=US/Eastern  
RUN ln --symbolic --no-dereference --force /usr/shared/zoneinfo/${TZ}
/etc/localtime && echo ${TZ} > /etc/timezone  
  
COPY ./gitconfig /root/.gitconfig  
  
ENV WORKSPACE=/workspace  
  
#################################################  
# Go(lang)  
#################################################  
  
ENV GOLANG_DOWNLOAD_URL=https://storage.googleapis.com/golang/go1.6.3.linux-
amd64.tar.gz  
ENV
GOLANG_DOWNLOAD_SHA256=cdde5e08530c0579255d6153b08fdb3b8e47caabbe717bc7bcd7561275a87aeb  
  
RUN curl -fsSL "${GOLANG_DOWNLOAD_URL}" -o golang.tar.gz \  
&& echo "${GOLANG_DOWNLOAD_SHA256} golang.tar.gz" | sha256sum --check \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH=${WORKSPACE}/go  
ENV PATH=$PATH:/usr/local/go/bin:${GOPATH}/bin  
  
#################################################  
# Node.js  
#################################################  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
#################################################  
# Neovim  
#################################################  
# Install vim-plug:  
RUN curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim  
  
# Copy Neovim configuration into the container:  
COPY ./init.vim /root/.config/nvim/  
# Install plug-ins and quit Neovim.  
# NOTE: \--cmd flag will run a command before the configuration is parsed.  
RUN nvim -c 'PlugInstall' -c 'UpdateRemotePlugins' -c 'qa!'  
# Install Go(lang) binaries:  
RUN nvim +GoInstallBinaries +qall; exit 0  
# Colorschemes in Neovim doesn't seem to work correctly without this.  
ENV TERM=xterm-256color  


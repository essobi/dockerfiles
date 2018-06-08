FROM ubuntu:18.04  
LABEL maintainer="Warren Spits <warren@spits.id.au>"  
LABEL description="Preconfigured development environment"  
  
ARG user="warren"  
ARG fullname="Warren Spits"  
ARG email="warren@spits.id.au"  
ARG timezone="Australia/Melbourne"  
RUN rm -rf /var/lib/apt/lists/* && apt-get update  
  
RUN apt-get install -y xz-utils  
RUN apt-get install -y openssh-server tmux zsh curl man-db sudo iputils-ping
locales \  
tzdata mosh xsel xclip htop strace ltrace lsof dialog vim-common  
RUN apt-get install -y aptitude software-properties-common  
RUN echo 'docker.io docker.io/restart boolean true' | debconf-set-selections  
RUN apt-get install -y docker.io docker-compose \  
ruby2.5 ruby2.5-dev \  
nodejs npm \  
python3-pip python3 \  
python-pip python \  
build-essential cmake autoconf exuberant-ctags silversearcher-ag  
RUN apt-get install -y ncurses-dev libsqlite3-dev tig  
RUN apt-get install -y golang golang-go.tools golang-1.10  
RUN update-alternatives --install /usr/bin/ruby ruby /usr/bin/ruby2.5 400  
  
COPY ca-certificates/ /usr/local/share/ca-certificates/  
RUN update-ca-certificates  
  
RUN add-apt-repository ppa:neovim-ppa/unstable && \  
apt-get update && apt-get install -y neovim && \  
update-alternatives --install /usr/bin/vi vi /usr/bin/nvim 60 && \  
update-alternatives --install /usr/bin/vim vim /usr/bin/nvim 60 && \  
update-alternatives --install /usr/bin/editor editor /usr/bin/nvim 60  
  
# Install dependencies for lastpass-cli  
RUN apt-get update && apt-get install -y \  
openssl libcurl4-openssl-dev libxml2 libssl-dev libxml2-dev pinentry-curses  
  
# Install git ppa for latest stable  
RUN add-apt-repository ppa:git-core/ppa \  
&& apt-get update && apt-get install -y git  
  
RUN mkdir /var/run/sshd  
EXPOSE 22  
RUN rm /etc/update-motd.d/*  
RUN ln -sf /usr/share/zoneinfo/$timezone /etc/localtime  
  
RUN apt-get install -y locales  
COPY locale.gen /etc/  
RUN locale-gen && update-locale LANG=en_AU.UTF-8  
  
RUN adduser $user \--disabled-password --shell /bin/zsh --gecos
"$fullname,,,,$email" && \  
usermod $user -G sudo,users -a && \  
passwd -d $user  
  
# Change the sudo config  
RUN perl -i -pe 's|(%sudo.*\s+)ALL$|$1NOPASSWD:ALL|g' /etc/sudoers \  
&& echo 'Defaults env_keep = "http_proxy https_proxy ftp_proxy DISPLAY
XAUTHORITY"' > /etc/sudoers.d/preserve_env¬  
  
COPY home/ /home/$user/  
RUN chown -R $user:$user /home/$user  
  
USER $user  
RUN git config --global user.name "$fullname" \  
&& git config --global user.email "$email"  
  
# Install oh-my-zsh  
RUN umask g-w,o-w; git clone \--depth 1 https://github.com/robbyrussell/oh-my-
zsh.git ~/.oh-my-zsh && \  
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-
zsh/custom/plugins/zsh-syntax-highlighting && \  
git clone https://github.com/Treri/fzf-zsh.git ~/.oh-my-
zsh/custom/plugins/fzf-zsh && \  
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc && \  
sed -i 's/^ZSH_THEME=.*/ZSH_THEME="blinks"/' ~/.zshrc && \  
perl -0pe 's/^(plugins=)\\(.*\\)/$1(gitfast gitignore ruby golang node docker
zsh-syntax-highlighting fzf-zsh)/ms' -i ~/.zshrc  
COPY zsh_custom/ /home/$user/.oh-my-zsh/custom  
  
# install fzf, tpm, python neovim, vim plugin manager  
RUN git clone https://github.com/junegunn/fzf.git ~/.fzf && ~/.fzf/install
--bin && \  
ln -s ~/.fzf ~/.oh-my-zsh/custom/plugins/fzf && \  
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm && \  
~/.tmux/plugins/tpm/bin/install_plugins && \  
pip3 install setuptools && pip3 install neovim && \  
pip install setuptools && pip install neovim && \  
curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs \  
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim  
  
# Install nvm with node and npm  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh |
bash \  
&& NVM_DIR=/home/$user/.nvm && . $NVM_DIR/nvm.sh \  
&& nvm install --lts node \  
&& npm config set cafile /etc/ssl/certs/ca-certificates.crt \  
&& npm install -g --upgrade npm  
RUN NVM_DIR=/home/$user/.nvm && . $NVM_DIR/nvm.sh \  
&& npm install -g yarn eslint_d javascript-typescript-langserver import-js  
  
ARG GOPATH=/home/$user/go  
RUN (echo export GOPATH=$GOPATH && \  
echo export PATH=\$GOPATH/bin:\$PATH && \  
echo export CDPATH=.:$GOPATH/src && \  
echo export FZF_DEFAULT_COMMAND=\'ag --nocolor -g \"\"\' ) >> ~/.zshrc  
  
RUN go get -v \  
github.com/github/hub \  
github.com/nsf/gocode \  
github.com/alecthomas/gometalinter \  
golang.org/x/tools/cmd/goimports \  
golang.org/x/tools/cmd/guru \  
golang.org/x/tools/cmd/gorename \  
github.com/golang/lint/golint \  
github.com/kisielk/errcheck \  
github.com/jstemmer/gotags \  
github.com/rogpeppe/godef \  
github.com/klauspost/asmfmt/cmd/asmfmt \  
github.com/fatih/motion \  
github.com/zmb3/gogetdoc \  
github.com/josharian/impl  
  
RUN nvim +PlugInstall +UpdateRemotePlugins +qa && \  
nvim +GoInstallBinaries +qa  
  
# Build lastpass-cli  
RUN git clone -b v1.3.0 https://github.com/lastpass/lastpass-cli.git
~/build/lastpass-cli && \  
cd ~/build/lastpass-cli && make  
  
USER root  
  
# Install lastpass-cli  
RUN cd /home/$user/build/lastpass-cli && make PREFIX=/usr/local install  
  
# Fix permissions  
RUN chown -R $user:$user /home/$user/.oh-my-zsh/custom  
  
CMD ["/usr/sbin/sshd", "-D"]  


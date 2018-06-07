FROM ubuntu:16.04  
LABEL maintainer="joshua7v@hotmail.com"  
  
ENV TERM xterm-256color  
ENV TZ Aisa/Shanghai  
ENV TMUX_VERSION 2.7  
ENV VIFM_VERSION 0.9  
ENV HOME /root  
ENV NODE_VERSION 10.1.0  
ENV ELIXIR_VERSION 1.6.1  
ENV ERLANG_VERSION 20.1  
ENV GOLANG_VERSION 1.9  
ENV PYTHON_VERSION 3.6.2  
ENV ELM_VERSION 0.18.0  
  
RUN ln -snf /bin/bash /bin/sh  
RUN apt-get update \  
&& apt-get install -y openssh-server \  
software-properties-common \  
apt-transport-https \  
ca-certificates \  
locales \  
tzdata \  
  
# Install build dependencies  
pkg-config \  
libevent-dev \  
ncurses-dev \  
build-essential \  
clang \  
automake \  
autoconf \  
libreadline-dev \  
libncurses-dev \  
libncursesw5-dev \  
libssl-dev \  
libyaml-dev \  
libxslt-dev \  
libffi-dev \  
libtool \  
unixodbc-dev \  
python3-dev \  
  
# Install tools  
silversearcher-ag \  
unzip \  
inotify-tools \  
tree \  
zsh \  
jq \  
curl \  
wget \  
git \  
man \  
iputils-ping \  
net-tools \  
iftop \  
iotop \  
htop \  
vim \  
  
# Install neovim  
&& add-apt-repository ppa:neovim-ppa/stable \  
&& apt-get update \  
&& apt-get install -y \  
neovim \  
  
&& mkdir /var/run/sshd \  
&& sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
\  
&& sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \  
&& echo 'root:root' |chpasswd \  
&& locale-gen en_US.UTF-8 \  
&& cd ~ \  
  
# Install vifm  
# && apt-key adv --recv-keys \--keyserver keyserver.ubuntu.com
0x908332071dd2e32e \  
# && echo "deb https://deb.best-hosting.cz/ubuntu/ xenial main" >
/etc/apt/sources.list.d/vifm.list \  
# bh-vifm \  
&& wget -O vifm-$VIFM_VERSION.tar.bz2
"http://prdownloads.sourceforge.net/vifm/vifm-$VIFM_VERSION.tar.bz2?download"
\  
&& tar --bzip -xvf vifm-$VIFM_VERSION.tar.bz2 \  
&& cd vifm-$VIFM_VERSION \  
&& ./configure && make && make install \  
&& cd ~ \  
&& rm -fr vifm-$VIFM_VERSION* \  
  
# Install rclone  
&& curl -O https://downloads.rclone.org/rclone-current-linux-amd64.zip \  
&& unzip rclone-current-linux-amd64.zip \  
&& cd rclone-*-linux-amd64 \  
&& cp rclone /usr/bin/ \  
&& mkdir -p /usr/local/share/man/man1 \  
&& cp rclone.1 /usr/local/share/man/man1/ \  
&& mandb \  
&& cd ~ \  
&& rm -fr rclone* \  
  
# Install tmux  
&& wget
https://github.com/tmux/tmux/releases/download/$TMUX_VERSION/tmux-$TMUX_VERSION.tar.gz
\  
&& tar -zxf tmux-$TMUX_VERSION.tar.gz \  
&& cd tmux-$TMUX_VERSION \  
&& ./configure && make \  
&& mv tmux /usr/bin/tmux \  
&& cd ~ \  
&& rm -fr tmux-$TMUX_VERSION* \  
  
# Install ctags  
&& git clone https://github.com/universal-ctags/ctags \  
&& cd ctags \  
&& ./autogen.sh \  
&& ./configure \  
&& make && make install \  
&& cd ~ \  
&& rm -fr ctags \  
  
# Install mongodb-org-shell tools  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 \  
&& echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.6 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.6.list \  
&& apt-get update && apt-get install -y mongodb-org-shell mongodb-org-tools \  
  
# Change to zsh  
&& chsh -s $(which zsh) \  
&& apt-get clean  
  
RUN git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.4.0 \  
&& source ~/.asdf/asdf.sh \  
&& asdf plugin-add nodejs \  
&& export GNUPGHOME="${ASDF_DIR:-$HOME/.asdf}/keyrings/nodejs" && mkdir -p
"$GNUPGHOME" && chmod 0700 "$GNUPGHOME" \  
&& bash ~/.asdf/plugins/nodejs/bin/import-release-team-keyring \  
&& asdf plugin-add erlang \  
&& asdf plugin-add elixir \  
&& asdf plugin-add golang \  
&& asdf plugin-add python \  
&& asdf plugin-add elm \  
&& asdf install nodejs $NODE_VERSION \  
&& asdf install erlang $ERLANG_VERSION \  
&& asdf install elixir $ELIXIR_VERSION \  
&& asdf install golang $GOLANG_VERSION \  
&& asdf install python $PYTHON_VERSION \  
&& asdf install elm $ELM_VERSION \  
&& asdf global nodejs $NODE_VERSION \  
&& asdf global erlang $ERLANG_VERSION \  
&& asdf global elixir $ELIXIR_VERSION \  
&& asdf global golang $GOLANG_VERSION \  
&& asdf global python $PYTHON_VERSION \  
&& asdf global elm $ELM_VERSION  
  
RUN curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh | bash \  
&& git clone git://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-
zsh/custom/plugins/zsh-autosuggestions \  
  
# Fix time zone  
&& echo $TZ > /etc/timezone \  
&& rm /etc/localtime \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get clean \  
  
# Set git differ  
&& curl -O https://raw.githubusercontent.com/so-fancy/diff-so-
fancy/master/third_party/build_fatpack/diff-so-fancy \  
&& chmod +x diff-so-fancy \  
&& mv diff-so-fancy /usr/local/bin/diff-so-fancy \  
&& git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX" \  
&& git config --global color.ui true \  
&& git config --global color.diff-highlight.oldNormal "red bold" \  
&& git config --global color.diff-highlight.oldHighlight "red bold 52" \  
&& git config --global color.diff-highlight.newNormal "green bold" \  
&& git config --global color.diff-highlight.newHighlight "green bold 22" \  
&& git config --global color.diff.meta "227" \  
&& git config --global color.diff.frag "magenta bold" \  
&& git config --global color.diff.commit "227 bold" \  
&& git config --global color.diff.old "red bold" \  
&& git config --global color.diff.new "green bold" \  
&& git config --global color.diff.whitespace "red reverse" \  
  
# Restore shell settings  
&& git clone https://github.com/joshua7v/dot-files ~/.dot-files \  
&& cp ~/.dot-files/bashrc ~/.bashrc \  
&& cp ~/.dot-files/bash_profile ~/.bash_profile \  
&& cp ~/.dot-files/zshrc ~/.zshrc \  
  
# Enable asdf  
&& source ~/.asdf/asdf.sh \  
&& echo -e '\nsource $HOME/.asdf/asdf.sh' >> ~/.zshrc \  
&& echo -e '\nsource $HOME/.asdf/completions/asdf.bash' >> ~/.zshrc \  
  
# Install elixir packages  
&& mix local.hex --force \  
&& mix local.rebar --force \  
&& mix archive.install
https://github.com/phoenixframework/archives/raw/master/phx_new.ez --force \  
&& git clone https://github.com/lpil/dogma \  
&& cd dogma \  
&& mix deps.get \  
&& mix escript.build \  
&& cp dogma /usr/local/bin/dogma \  
&& cd .. \  
&& rm -fr dogma \  
  
# Install go packages  
&& echo 'export GOPATH=$HOME/.go' >> .bashrc \  
&& echo 'export PATH=$GOPATH/bin:/usr/local/go/bin:$PATH' >> .bashrc \  
&& go get -u github.com/nsf/gocode \  
  
# Install python packages  
&& pip install --upgrade pip \  
&& pip install pgcli neovim jedi \  
  
# Install js / ts / elm packages  
# && curl -o\- -L https://yarnpkg.com/install.sh | bash \  
&& npm i -g --unsafe-perm=true --allow-root \  
tern \  
typescript \  
ts-node \  
typeorm \  
npm-check-updates \  
create-react-app \  
create-elm-app \  
@angular/cli \  
elm-format \  
elm-live \  
eslint \  
tslint \  
prettier \  
pug-beautifier \  
express-generator \  
serve \  
aglio \  
  
# Restore neovim settings  
&& mkdir -p ~/.config/nvim \  
&& cp ~/.dot-files/neovim/init.vim ~/.config/nvim/init.vim \  
&& curl
https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh >
installer.sh \  
&& bash ./installer.sh ~/.config/nvim \  
&& rm installer.sh \  
&& sed -i "/filetype\ plugin\ indent\ on/ilet g:dein#install_progress_type =
'none'\nlet g:dein#install_message_type = 'none'\n" ~/.config/nvim/init.vim \  
&& sed -i "/'build':\ 'make'/d" ~/.config/nvim/init.vim \  
&& nvim +"call dein#install()" +qall \  
# && cd ~/.config/nvim/plugged/repos/github.com/zchee/deoplete-
go/rplugin/python3/deoplete/ujson/ \  
# && python3 setup.py build --build-
base=/root/.config/nvim/plugged/repos/github.com/zchee/deoplete-go/build
--build-lib=/root/.config/nvim/plugged/repos/github.com/zchee/deoplete-
go/build \  
&& cd ~ \  
&& cp ~/.dot-files/neovim/init.vim ~/.config/nvim/init.vim \  
  
# Restore user settings  
&& cp ~/.dot-files/tern-project ~/.tern-project \  
&& cp ~/.dot-files/editorconfig ~/.editorconfig \  
&& cp -r ~/.dot-files/ctags.d ~/.ctags.d \  
  
# Restore vifm settings  
&& cp -r ~/.dot-files/vifm ~/.config/vifm \  
  
# Restore tmux settings  
&& cp ~/.dot-files/tmux.conf ~/.tmux.conf \  
&& git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm \  
&& ~/.tmux/plugins/tpm/bin/install_plugins \  
&& sed -i $'$i set -g @resurrect-dir \'/data/.tmux/resurrect\'' ~/.tmux.conf  
  
EXPOSE 22 3000  
ENTRYPOINT ["/usr/sbin/sshd", "-D"]  
VOLUME ["/data"]  
  


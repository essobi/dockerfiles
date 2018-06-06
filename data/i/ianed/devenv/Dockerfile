FROM alpine:latest  
  
MAINTAINER IanEdington <IanEdington@gmail.com>  
ENV LastUpdate 2016-11-13-21-47  
RUN echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories \  
&& echo '@community http://dl-cdn.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories \  
&& echo '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories  
  
RUN apk update \  
&& apk upgrade \  
&& apk add \  
bash \  
build-base \  
curl \  
ctags \  
cmake \  
ctags \  
editorconfig@community \  
git \  
go \  
llvm \  
lua \  
luajit \  
make \  
# mono \  
ncurses \  
ncurses-dev \  
ncurses-terminfo \  
nodejs \  
python \  
python-dev \  
python3 \  
python3-dev \  
perl \  
perl-dev \  
ruby \  
rust@testing \  
the_silver_searcher \  
zsh \  
libice \  
libgcc \  
libstdc++ \  
libsm \  
libuv \  
libx11 \  
libx11-dev \  
libxpm-dev \  
libxt \  
libxt-dev  
  
# BUILD VIM  
# VIM compiler expects python3 to hav a config folder  
RUN ln -s /usr/lib/python3.5/config-3.5m/ /usr/lib/python3.5/config  
  
# Clone  
RUN git clone \--depth 1 https://github.com/vim/vim.git /tmp/vim  
  
# Build  
WORKDIR /tmp/vim  
RUN ./configure --with-features=huge \  
\--enable-multibyte \  
\--enable-rubyinterp=yes \  
\--enable-pythoninterp=yes \  
\--with-python-config-dir=/usr/lib/python2.7/config \  
\--enable-python3interp=yes \  
\--with-python3-config-dir=/usr/lib/python3.5/config \  
\--enable-perlinterp=yes \  
\--enable-luainterp=yes \  
\--enable-rubyinterp=yes \  
\--with-luajit \  
\--disable-gui \  
\--enable-cscope \  
\--prefix=/usr  
RUN make VIMRUNTIMEDIR=/usr/share/vim/vim80  
RUN make install  
WORKDIR /  
  
# Set environment variables  
ENV PATH $PATH:$GOBIN:$GOPATH/bin:$NODEBIN  
RUN mkdir -p /home/developer/workspace  
ENV HOME /home/developer  
ENV GOPATH /home/developer/workspace  
ENV GOROOT /usr/lib/go  
ENV GOBIN $GOROOT/bin  
ENV NODEBIN /usr/lib/node_modules/bin  
ENV TERM screen-256color  
  
ENTRYPOINT ["/bin/zsh"]  
WORKDIR $HOME  
  
# install dotfiles  
RUN git clone \--depth 1 https://gitlab.com/IanEdington/dotfiles.git
~/.dotfiles  
  
# add npm dependencies  
RUN npm install -g eslint jshint typescript  
  
# symlink dotfiles  
RUN ln -s ~/.dotfiles/zsh ~/.zsh  
RUN ln -s ~/.zsh/zshenv ~/.zshenv  
RUN ln -s ~/.zsh/zshrc ~/.zsh/.zshrc  
RUN ln -s ~/.dotfiles/vim ~/.vim  
RUN ln -s ~/.vim/vimrc ~/.vimrc  
RUN ln -s ~/.vim/editorconfig ~/.editorconfig  
RUN mkdir -p ~/.config/git  
RUN ln -s ~/.dotfiles/git/config ~/.config/git/config  
RUN ln -s ~/.dotfiles/git/ignore ~/.config/git/ignore  
  
# download and install prezto for zsh  
RUN git clone \--depth 1 https://github.com/sorin-ionescu/prezto.git
~/.zsh/.zprezto \  
&& cd ~/.zsh/.zprezto \  
&& git submodule update --init --remote --recursive  
RUN ln -s ~/.zsh/.zprezto/runcoms/zlogin ~/.zsh/.zlogin  
RUN ln -s ~/.zsh/.zprezto/runcoms/zlogout ~/.zsh/.zlogout  
RUN ln -s ~/.zsh/.zprezto/runcoms/zpreztorc ~/.zsh/.zpreztorc  
RUN ln -s ~/.zsh/.zprezto/runcoms/zprofile ~/.zsh/.zprofile  
  
# download and install vundle for vim  
RUN git clone \--depth 1 https://github.com/VundleVim/Vundle.vim.git
~/.vim/bundle/Vundle.vim \  
&& cd ~/.vim/bundle/Vundle.vim \  
&& git submodule update --init --remote --recursive  
RUN vim -E -u NONE -S ~/.vim/start_vundle.zshrc +PluginInstall +qall  
  
# Build YouCompleteMe  
RUN cd ~/.vim/bundle/YouCompleteMe \  
&& ./install.py --gocode-completer --tern-completer  
  
# Java  
ENV JAVA_HOME=/usr/lib/jvm/default-jvm  
ENV CLASSPATH=.  
RUN apk add --no-cache \  
openjdk8 \  
junit \  
&& ln -sf "${JAVA_HOME}/bin/"* "/usr/bin/"  


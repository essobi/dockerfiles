FROM golang:alpine  
MAINTAINER Gerson Graciani  
  
#Copies .vimrc to root  
ADD /root/ /root/  
  
  
RUN \  
#Adding GIT and BUILD Tools AND ncurses-dev  
apk --update add git build-base ncurses-dev lua5.2-libs lua5.2 lua5.2-posix
autoconf automake libtool libstdc++ \  
#Getting Go Tools  
&& go get golang.org/x/tools/cmd/godoc \  
&& go get github.com/nsf/gocode \  
&& go get golang.org/x/tools/cmd/goimports \  
&& go get github.com/rogpeppe/godef \  
&& go get golang.org/x/tools/cmd/oracle \  
&& go get golang.org/x/tools/cmd/gorename \  
&& go get github.com/golang/lint/golint \  
&& go get github.com/kisielk/errcheck \  
&& go get github.com/jstemmer/gotags \  
&& go get -u github.com/golang/protobuf/protoc-gen-go \  
  
#Compiling Google Protobuf  
&& cd /tmp \  
&& wget
https://github.com/google/protobuf/releases/download/v3.0.0-beta-2/protobuf-
cpp-3.0.0-beta-2.tar.gz \  
&& tar xvzf protobuf-cpp-3.0.0-beta-2.tar.gz \  
&& cd protobuf-3.0.0-beta-2/ \  
&& ./autogen.sh \  
&& ./configure \  
&& make && make check && make install && make clean \  
  
#Compiling VIM  
&& cd /tmp \  
&& git clone https://github.com/vim/vim.git \  
&& cd vim \  
&& ./configure --with-features=huge --enable-luainterp \  
\--enable-gui=no \--without-x \--prefix=/usr \  
&& make VIMRUNTIMEDIR=/usr/share/vim/vim74 \  
&& make install \  
#CLEANUP  
&& apk del libtool automake autoconf build-base\  
&& rm -rf /var/cache/apk/* /tmp/* /var/tmp/* /go/src/*  
  
#CONFIG VIM  
RUN \  
mkdir -p /root/.vim/bundle \  
&& cd /root/.vim/bundle \  
&& git clone --depth 1 https://github.com/gmarik/Vundle.vim.git \  
&& git clone --depth 1 https://github.com/fatih/vim-go.git \  
&& git clone --depth 1 https://github.com/majutsushi/tagbar.git \  
&& git clone --depth 1 https://github.com/Shougo/neocomplete.vim.git \  
&& git clone --depth 1 https://github.com/bling/vim-airline.git \  
&& git clone --depth 1 https://github.com/tpope/vim-fugitive.git \  
&& git clone --depth 1 https://github.com/jistr/vim-nerdtree-tabs.git \  
&& git clone --depth 1 https://github.com/mbbill/undotree.git \  
&& git clone --depth 1 https://github.com/Lokaltog/vim-easymotion.git \  
&& git clone --depth 1 https://github.com/scrooloose/nerdcommenter.git \  
&& git clone --depth 1 https://github.com/scrooloose/nerdtree.git \  
&& vim +PluginInstall +qall \  
#CLEANUP  
&& rm -rf */.git  


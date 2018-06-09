FROM centos:7  
  
MAINTAINER Haifeng Zhang "zhanghf@zailingtech.com"  
  
# 设置go相关环境变量  
ENV GOLANG_VERSION 1.9.2  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
# 设置locale，进入终端可以输入中文  
ENV LANG en_US.utf8  
# 设置容器时区  
ENV TZ "Asia/Shanghai"  
  
RUN yum update -y \  
# 安装开发工具包和man  
&& yum install -y epel-release.noarch \  
&& yum -y groupinstall "Development Tools" \  
&& yum -y install gitflow \  
&& yum -y install valgrind \  
&& yum -y install man \  
# 安装zsh和oh-my-zsh  
&& yum install -y zsh \  
&& yum install -y which \  
&& git clone --depth=1 https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-
zsh \  
&& chsh -s /bin/zsh \  
# 安装vim需要的工具包  
&& yum install -y cmake \  
&& yum install -y clang \  
&& yum install -y clang-devel.x86_64 \  
&& yum install -y llvm-devel.x86_64 \  
&& yum install -y openssl \  
&& yum install -y cscope \  
&& yum install -y python \  
&& yum install -y python-devel \  
&& yum install -y ruby \  
&& yum install -y ruby-devel \  
&& yum install -y lua \  
&& yum install -y lua-devel \  
&& yum install -y perl \  
&& yum install -y tcl \  
&& yum install -y tcl-devel \  
&& yum install -y ncurses \  
&& yum install -y ncurses-devel \  
&& yum install -y the_silver_searcher \  
&& yum install -y tmux \  
&& yum install -y python34 \  
&& yum install -y python34-devel \  
&& yum install -y libtool \  
&& yum install -y autoconf \  
&& yum install -y automake \  
&& yum install -y pkgconfig \  
&& yum install -y unzip \  
&& yum install -y wget \  
&& yum clean all \  
# 安装go  
&& goRelArch='linux-amd64' \  
&& url="https://golang.org/dl/go${GOLANG_VERSION}.${goRelArch}.tar.gz" \  
&& wget -O go.tgz "$url" \  
&& tar -C /usr/local -xzf go.tgz \  
&& rm go.tgz \  
&& go version \  
&& go get github.com/klauspost/asmfmt/cmd/asmfmt \  
&& go get github.com/kisielk/errcheck \  
&& go get github.com/davidrjenni/reftools/cmd/fillstruct \  
&& go get github.com/nsf/gocode \  
&& go get github.com/rogpeppe/godef \  
&& go get github.com/zmb3/gogetdoc \  
&& go get golang.org/x/tools/cmd/goimports \  
&& go get github.com/golang/lint/golint \  
&& go get github.com/alecthomas/gometalinter \  
&& go get github.com/fatih/gomodifytags \  
&& go get golang.org/x/tools/cmd/gorename \  
&& go get github.com/jstemmer/gotags \  
&& go get golang.org/x/tools/cmd/guru \  
&& go get github.com/josharian/impl \  
&& go get github.com/dominikh/go-tools/cmd/keyify \  
&& go get github.com/fatih/motion \  
&& go get -u github.com/golang/dep/cmd/dep \  
&& go get -u github.com/cweill/gotests/...  
  
# 安装vim  
COPY .vimrc /root/  
  
RUN cd /usr/local/src \  
&& git clone https://github.com/vim/vim.git \  
&& cd vim \  
&& git checkout v8.0.1300 \  
&& ./configure --prefix=/usr \  
\--with-features=huge \  
\--enable-multibyte \  
\--enable-cscope=yes \  
\--enable-luainterp=yes \  
\--enable-rubyinterp=yes \  
\--enable-pythoninterp=yes \  
\--with-python-config-dir=/usr/lib64/python2.7/config/ \  
\--with-python3-config-dir=/usr/lib64/python3.4/config-3.4m \  
\--enable-python3interp=yes \  
\--enable-tclinterp=yes \  
\--enable-gui=auto \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf vim/ \  
# 安装powerline字体  
&& git clone https://github.com/powerline/fonts.git \  
&& cd fonts \  
&& ./install.sh \  
&& cd .. \  
&& rm -rf fonts/ \  
# 安装rtags用于C++跳转  
&& wget https://andersbakken.github.io/rtags-releases/rtags-2.16.tar.gz \  
&& tar zxvf rtags-2.16.tar.gz \  
&& cd rtags-2.16 \  
&& cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 . \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf rtags-2.16/ \  
&& rm -rf rtags-2.16.tar.gz \  
# 安装bear用于通过Makefile生成JSON compilation database  
&& git clone https://github.com/rizsotto/Bear.git \  
&& cd Bear \  
&& git checkout 2.2.1 \  
&& cmake . \  
&& make all \  
&& make install \  
&& cd .. \  
&& rm -rf Bear \  
# 安装vim初次启动需要的插件  
&& git clone https://github.com/tomasr/molokai.git ~/.vim/bundle/molokai \  
&& git clone https://github.com/Shougo/unite.vim.git ~/.vim/bundle/unite.vim \  
&& git clone https://github.com/shougo/vimfiler.vim.git
~/.vim/bundle/vimfiler.vim \  
# vim其他插件安装  
&& vim +PlugInstall +qall  
  
COPY .tmux.conf /root/  
COPY .zshrc /root/  
  
#work dir  
WORKDIR /work  
  
#cmd  
CMD zsh  


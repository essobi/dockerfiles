FROM golang:1.8.3  
MAINTAINER Gerson Graciani  
  
  
#Build and install vim  
RUN apt-get update -y \  
&& apt-get install -y ncurses-dev libtolua-dev exuberant-ctags unzip \  
&& ln -s /usr/include/lua5.2/ /usr/include/lua \  
&& ln -s /usr/lib/x86_64-linux-gnu/liblua5.2.so /usr/lib/liblua.so \  
&& cd /tmp \  
&& git clone https://github.com/vim/vim.git \  
&& cd vim \  
&& ./configure --with-features=huge --enable-luainterp \  
\--enable-gui=no \--without-x \--prefix=/usr \  
&& make VIMRUNTIMEDIR=/usr/share/vim/vim80 \  
&& make install \  
&& rm -rf /tmp/* /var/tmp/* \  
&& apt-get clean  
  
#CONFIGURE VIM  
RUN mkdir -p /root/.vim/bundle \  
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
&& rm -rf */.git  
  
#Getting Go Tools  
RUN /bin/true \  
&& go get golang.org/x/tools/cmd/guru \  
&& go get golang.org/x/tools/cmd/goimports \  
&& go get golang.org/x/tools/cmd/godoc \  
&& go get golang.org/x/tools/cmd/gorename \  
&& go get github.com/golang/lint/golint \  
&& go get github.com/alecthomas/gometalinter \  
&& go get github.com/klauspost/asmfmt/cmd/asmfmt \  
&& go get github.com/fatih/motion \  
&& go get github.com/zmb3/gogetdoc \  
&& go get github.com/josharian/impl \  
&& go get github.com/nsf/gocode \  
&& go get github.com/rogpeppe/godef \  
&& go get github.com/kisielk/errcheck \  
&& go get github.com/jstemmer/gotags \  
&& go get github.com/govend/govend \  
&& go get google.golang.org/grpc \  
&& go get -u github.com/golang/protobuf/proto \  
&& go get -u github.com/golang/protobuf/protoc-gen-go \  
&& go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway \  
&& go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger \  
&& go get -u github.com/golang/protobuf/protoc-gen-go \  
&& go get -u github.com/smartystreets/goconvey/convey \  
&& go get github.com/DATA-DOG/godog/cmd/godog \  
&& go get github.com/DATA-DOG/go-sqlmock \  
&& go get github.com/satori/go.uuid \  
&& /bin/true  
  
#Copies .vimrc to root  
ADD root/ /root/  
ADD etc/ /etc/  
RUN vim +PluginInstall +qall  
#ENTRYPOINT ["vim", "+PluginInstall", "+qall"]  
  
#INstalling Google Protobuffer  
RUN /bin/true \  
&& cd /tmp \  
&& curl -OL
https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip
\  
&& mkdir -p /opt/protoc-3.3 \  
&& cd /opt/protoc-3.3 \  
&& unzip /tmp/protoc-3.3.0-linux-x86_64.zip \  
&& /bin/true  
  
#Installing docker  
ENV COMPOSE_VERSION=1.14.0  
RUN /usr/bin/curl https://get.docker.com/ | /bin/bash \  
&& sh -c "curl -L
https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose" \  
&& chmod +x /usr/local/bin/docker-compose \  
&& sh -c "curl -L
https://raw.githubusercontent.com/docker/compose/${COMPOSE_VERSION}/contrib/completion/bash/docker-
compose > /etc/bash_completion.d/docker-compose"  
  
ENV JAVA_HOME=/usr/local/java/jdk1.8.0_131  
ENV PATH=/opt/protoc-3.3/bin:$JAVA_HOME/bin:/usr/local/bin:$PATH  
  
#Installing buildr/java/ruby  
RUN apt-get install -y ruby-full \  
&& mkdir -p /usr/local/java \  
&& cd /usr/local/java \  
&& wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz
\  
&& tar xvzf jdk-8u131-linux-x64.tar.gz \  
&& gem install buildr  
  
  
  
CMD ["bash"]  


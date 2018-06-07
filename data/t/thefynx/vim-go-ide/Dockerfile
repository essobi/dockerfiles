FROM golang  
MAINTAINER Levi Smith  
  
ADD dotfiles/ /  
ENV DEVHOME /home/dev  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
  
# install pagkages  
RUN apt-get update && \  
apt-get install -y sudo ncurses-dev libtolua-dev \  
exuberant-ctags pandoc lynx && \  
ln -s /usr/include/lua5.2/ /usr/include/lua && \  
ln -s /usr/lib/x86_64-linux-gnu/liblua5.2.so /usr/lib/liblua.so && \  
cd /tmp && \  
# build and install vim  
git clone https://github.com/vim/vim.git && \  
cd vim && \  
./configure --with-features=huge --enable-luainterp \  
\--enable-gui=no \--without-x \--prefix=/usr && \  
make VIMRUNTIMEDIR=/usr/share/vim/vim74 && \  
make install && \  
# get go tools  
go get golang.org/x/tools/cmd/godoc && \  
go get github.com/nsf/gocode && \  
go get github.com/derekparker/delve/cmd/dlv && \  
go get golang.org/x/tools/cmd/goimports && \  
go get github.com/rogpeppe/godef && \  
go get golang.org/x/tools/cmd/oracle && \  
go get golang.org/x/tools/cmd/gorename && \  
go get github.com/golang/lint/golint && \  
go get github.com/kisielk/errcheck && \  
go get github.com/jstemmer/gotags && \  
curl https://glide.sh/get | sh && \  
mv /go/bin/* /usr/local/go/bin && \  
# add dev user  
mkdir -p /project && \  
adduser dev --disabled-password --gecos "" && \  
chown -R dev:dev $DEVHOME /go /project && \  
echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
# cleanup  
rm -rf /go/src/* /go/pkg && \  
apt-get remove -y ncurses-dev && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER dev  
  
# install vim plugins  
RUN mkdir -p $DEVHOME/.vim/bundle && \  
git clone https://github.com/gmarik/vundle \  
$DEVHOME/.vim/bundle/vundle && \  
vim +PluginInstall +qall!  
  
VOLUME /project  
  
WORKDIR /project  
  
CMD /bin/bash -c /usr/bin/vim  


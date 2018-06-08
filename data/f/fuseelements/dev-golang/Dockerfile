FROM golang:1.5-wheezy  
  
# install pagkages  
RUN apt-get update && \  
apt-get install -y ncurses-dev libtolua-dev python-dev exuberant-ctags && \  
ln -s /usr/include/lua5.2/ /usr/include/lua && \  
ln -s /usr/lib/x86_64-linux-gnu/liblua5.2.so /usr/lib/liblua.so && \  
# build and install vim  
cd /tmp && \  
hg clone https://code.google.com/p/vim/ && \  
cd vim && \  
./configure --with-features=huge --enable-multibyte \  
\--enable-cscope \--enable-luainterp --enable-pythoninterp \  
\--enable-gui=no \--without-x \--prefix=/usr && \  
make VIMRUNTIMEDIR=/usr/share/vim/vim74 && \  
make install && \  
# get go tools  
go get golang.org/x/tools/cmd/godoc && \  
go get github.com/nsf/gocode && \  
go get golang.org/x/tools/cmd/goimports && \  
go get github.com/rogpeppe/godef && \  
go get golang.org/x/tools/cmd/oracle && \  
go get golang.org/x/tools/cmd/gorename && \  
go get github.com/golang/lint/golint && \  
go get github.com/kisielk/errcheck && \  
go get github.com/jstemmer/gotags && \  
go get github.com/monochromegane/the_platinum_searcher/... && \  
mv /go/bin/* /usr/local/go/bin && \  
# add "me" user  
adduser me \--disabled-password --gecos "" && \  
echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
# set-up the time zone  
cp /usr/share/zoneinfo/America/New_York /etc/localtime && \  
# cleanup  
rm -rf /go/src/* /go/pkg && \  
apt-get remove -y ncurses-dev && \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY home_me/ /home/me/  
  
# install vim plugins  
RUN mkdir -p /home/me/.vim/bundle && \  
mkdir -p /home/me/.vim/autoload && \  
cd /home/me/.vim/autoload && \  
wget -q https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim
&& \  
cd /home/me/.vim/bundle && \  
git clone --depth 1 https://github.com/bling/vim-airline.git && \  
git clone --depth 1 https://github.com/altercation/vim-colors-solarized.git &&
\  
git clone --depth 1 \--branch v1.3 https://github.com/tpope/vim-dispatch.git
&& \  
git clone --depth 1 \--branch v2.1.1 https://github.com/Lokaltog/vim-
easymotion.git && \  
git clone --depth 1 https://github.com/tpope/vim-fugitive.git && \  
git clone --depth 1 https://github.com/airblade/vim-gitgutter.git && \  
git clone --depth 1 \--branch v1.1 https://github.com/fatih/vim-go.git && \  
git clone --depth 1 \--branch v2.0.0
https://github.com/haya14busa/incsearch.vim.git && \  
git clone --depth 1 https://github.com/tpope/vim-markdown.git && \  
git clone --depth 1 \--branch ver.2.1
https://github.com/Shougo/neocomplete.vim.git && \  
git clone --depth 1 https://github.com/scrooloose/nerdcommenter.git && \  
git clone --depth 1 https://github.com/scrooloose/nerdtree.git && \  
git clone --depth 1 \--branch 3.6.0
https://github.com/scrooloose/syntastic.git && \  
git clone --depth 1 https://github.com/majutsushi/tagbar.git && \  
git clone --depth 1 https://github.com/SirVer/ultisnips.git && \  
git clone --depth 1 https://github.com/Shougo/unite.vim.git && \  
git clone --depth 1 \--branch ver.8.0
https://github.com/Shougo/vimproc.vim.git && \  
cd /home/me/.vim/bundle/vimproc.vim && \  
make && \  
# cleanup  
rm -rf vim-airline/.git \  
vim-colors-solarized/.git \  
vim-easymotion/.git \  
vim-fugitive/.git \  
vim-gitgutter/.git \  
vim-go/.git \  
incsearch.vim/.git \  
vim-markdown.vim/.git \  
neocomplete.vim/.git \  
nerdcommenter/.git \  
nerdtree/.git \  
syntastic/.git \  
tagbar/.git \  
ultisnips/.git \  
unite/.git \  
vimproc.vim/.git && \  
chown -R me:me /home/me /go  
  
USER me  
ENV HOME=/home/me \  
TERM=xterm-256color  


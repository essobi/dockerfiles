FROM birchwoodlangham/ubuntu-base-atom:1.24.0  
  
RUN apt-get update && \  
apt-get install -y -qq --fix-missing python-pip powerline && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
pip install --upgrade pip && \  
pip install psutil thefuck && \  
useradd -d /home/user -m -U user && \  
wget https://dl.google.com/go/go1.10.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.10.linux-amd64.tar.gz && \  
rm go1.10.linux-amd64.tar.gz  
  
USER user  
WORKDIR /home/user  
  
# Use this one to install the plugins etc.  
COPY vimrc_plugins /home/user/.vimrc  
  
# Now for vim plugins, the powerline fonts and nerd fonts required for
powerline  
RUN git clone https://github.com/powerline/fonts.git && \  
fonts/install.sh && \  
rm -rf fonts && \  
git clone --depth 1 https://github.com/ryanoasis/nerd-fonts.git fonts && \  
cd /home/user/fonts && \  
./install.sh -q --copy \--complete && \  
cd /home/user && \  
rm -rf fonts && \  
mkdir -p /home/user/.vim && \  
git clone https://github.com/VundleVim/Vundle.vim.git
/home/user/.vim/bundle/Vundle.vim && \  
vim +PluginInstall +qall && \  
export GOPATH=$HOME/go && \  
export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin && \  
go get -u golang.org/x/tools/cmd/goimports && \  
go get -u golang.org/x/tools/cmd/gorename && \  
go get -u github.com/sqs/goreturns && \  
go get -u github.com/nsf/gocode && \  
go get -u github.com/alecthomas/gometalinter && \  
go get -u github.com/zmb3/gogetdoc && \  
go get -u github.com/zmb3/goaddimport && \  
go get -u github.com/rogpeppe/godef && \  
go get -u golang.org/x/tools/cmd/guru && \  
go get -u github.com/fatih/gomodifytags && \  
go get -u github.com/tpng/gopkgs && \  
go get -u github.com/derekparker/delve/cmd/dlv && \  
go get -u github.com/sourcegraph/go-langserver && \  
/usr/bin/apm install go-plus go-debug atom-ide-ui ide-go  
  
VOLUME ["/home/user/go", "/home/user/.atom"]  
  
CMD ["/usr/bin/atom", "-f"]  


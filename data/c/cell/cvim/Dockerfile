FROM ubuntu:rolling as golang  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -qy
wget git ca-certificates  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy golang-go  
  
ENV GOPATH=/tmp/go GOBIN=/usr/local/go/bin PATH=${PATH}:/usr/local/go/bin  
RUN go get -u golang.org/x/tools/cmd/godoc  
RUN go get -u golang.org/x/tools/cmd/goimports  
RUN go get -u golang.org/x/tools/cmd/gorename  
  
RUN go get -u github.com/nsf/gocode  
RUN go get -u github.com/rogpeppe/godef  
RUN go get -u github.com/golang/lint/golint  
RUN go get -u github.com/kisielk/errcheck  
RUN go get -u github.com/jstemmer/gotags  
RUN go get -u github.com/golang/dep/cmd/dep  
  
RUN go get -u github.com/Originate/git-town  
RUN go get -u mvdan.cc/sh/cmd/shfmt  
  
FROM cell/playground  
ENV DOCKER_IMAGE="cell/cvim"  
ENV DEFAULT_CMD=vim  
  
#go  
COPY \--from=golang /usr/local/go /usr/local/go  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt install -qy golang-go &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/*  
  
#vim from vim-go  
COPY material/vimrc /etc/skel/.vimrc  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -qy vim-nox git exuberant-ctags
silversearcher-ag &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
git clone \--depth 1 https://github.com/junegunn/fzf.git /etc/skel/.fzf &&\  
/etc/skel/.fzf/install --bin &&\  
git clone \--depth 1 https://github.com/gmarik/Vundle.vim.git
/etc/skel/.vim/bundle/Vundle.vim &&\  
rm -rf /etc/skel/.vim/bundle/Vundle.vim/.git &&\  
ln -s /etc/skel/.vim /root/ &&\  
vim -u /etc/skel/.vimrc +PluginInstall +qall \  
vim -u /etc/skel/.vimrc +GoInstallBinaries +qall  
  
#Material  
COPY material/scripts /usr/local/bin/  
COPY material/payload /opt/payload/  
COPY material/profile.d /etc/profile.d/  
  


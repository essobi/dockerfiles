FROM alpine:latest  
  
ENV GOPATH=/root/go  
  
RUN \  
apk add \--update openssh-client vim nodejs zsh git python go \  
&& \  
env git clone --depth=1 https://github.com/robbyrussell/oh-my-zsh $HOME/.oh-
my-zsh \  
&& \  
mkdir $GOPATH && \  
go get github.com/constabulary/gb  
  
# other apps to consider:  
# https://github.com/mksenzov/i.js  
# https://github.com/danielgtaylor/nesh  
# https://github.com/jakubroztocil/httpie  
# https://github.com/foreverjs/forever  
# https://github.com/srsudar/eg  
# https://github.com/philovivero/distribution  
# https://github.com/facebook/PathPicker  
# https://github.com/paul-nechifor/ohmu  
# https://github.com/orf/gping  
# https://github.com/emre/storm  
# https://github.com/jamesob/desk  
  
ENV DOTFILE_PATH=/root/.dots \  
DOTFILE_REPO=https://github.com/dudymas/dots.git \  
DOTFILE_VIMRC=vimrc \  
DOTFILE_ZSHRC=.zshrc \  
PACKAGE_MANAGER=apk \  
ADD_PACKAGE_COMMAND="add" \  
REM_PACKAGE_COMMAND="del" \  
ZSH_THEME=random  
  
RUN git clone $DOTFILE_REPO $DOTFILE_PATH  
  
COPY files /  
  
RUN /setup.sh  
  
CMD /bin/zsh  


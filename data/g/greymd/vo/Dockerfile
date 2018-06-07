FROM alpine:3.5  
  
MAINTAINER Gre <greengregson@gmail.com>  
  
RUN apk --update \--no-cache add ca-certificates git vim curl && \  
rm -rf /var/cache/apk/* && \  
# ------------------  
# Set dotfiles  
# ------------------  
mkdir -p $HOME/repos/greymd && \  
git clone https://github.com/greymd/dotfiles.git $HOME/repos/greymd/dotfiles
&& \  
cd $HOME/repos/greymd/dotfiles && \  
# Delete existing dotfiles  
ls -a | grep '^\\.' | grep -vFw '.' | grep -v '^\\.git$' | sed 's|^|rm -f
$HOME/|' | sh && \  
# Set links  
ls -a | grep '^\\.' | grep -v '^\\.git$' | grep -vwF '.' | sed 's/^.*/echo ln
-s $(pwd)\/& $HOME\/&/' | sh | sh && \  
  
# ------------------  
# Set dein  
# ------------------  
curl -L
https://raw.githubusercontent.com/greymd/dockerfiles/master/vim/alpine/.vimrc
> $HOME/.vimrc && \  
mkdir -p $HOME/.cache/dein && \  
curl -L
https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh >
$HOME/installer.sh && \  
sh $HOME/installer.sh $HOME/.cache/dein && \  
yes | /usr/bin/vim -c ":silent call dein#install() | :q"  


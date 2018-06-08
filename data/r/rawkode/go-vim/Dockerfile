FROM golang:1-alpine  
  
RUN apk update \  
&& apk add vim curl git \  
&& curl -fLo ~/.vim/autoload/plug.vim --create-dirs \  
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim  
  
COPY vimrc /root/.vimrc  
  
RUN vim -E -u NONE -S ~/.vimrc +PlugInstall +qall  
  
WORKDIR /go/src/glasgow-pair-programming  


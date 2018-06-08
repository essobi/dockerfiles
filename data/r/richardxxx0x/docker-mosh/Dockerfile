FROM ubuntu:14.04  
MAINTAINER Richard Liu <richardxxx0x@gmail.com>  
RUN sudo apt-get update  
RUN sudo apt-get -y install mosh zsh git git-flow vim  
RUN sudo chsh -s `which zsh`  
RUN curl -L https://raw.github.com/robbyrussell/oh-my-
zsh/master/tools/install.sh | sh  
ADD ./scripts/vimrc /root/.vimrc


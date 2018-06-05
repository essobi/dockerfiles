FROM ubuntu:latest  
MAINTAINER Casey Webb <notcaseywebb@gmail.com>  
  
RUN apt-get update && apt-get install -y build-essential git curl wget zsh vim
nano  
RUN export TERM=linux; sh -c "$(wget
https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -) || true"  
RUN mkdir -p /root/.oh-my-zsh/custom/themes && touch /root/.z  
  
COPY .zshrc /root/.zshrc  
COPY .zsh-theme /root/.oh-my-zsh/custom/themes/custom.zsh-theme  
  
RUN echo "local devenv=bare" >> /root/.oh-my-zsh/custom/themes/custom.zsh-
theme  
  
WORKDIR /src  
  
ENTRYPOINT ["/usr/bin/zsh"]  


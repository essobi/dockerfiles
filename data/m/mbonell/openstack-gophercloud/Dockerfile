# Dockerfile for building a development environment to work with the  
# OpenStack Golang SDK Gophercloud to create cloud native applications.  
  
FROM ubuntu:16.04  
MAINTAINER Marcela Bonell <marcelabonell@gmail.com>  
  
# Update the repository sources list and install dependencies  
RUN apt-get update && apt-get install -y \  
vim \  
git \  
curl  
  
# Installing Golang environment  
RUN curl -O https://storage.googleapis.com/golang/go1.7.5.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzf go1.7.5.linux-amd64.tar.gz  
  
ENV GOPATH=/go-workspace  
ENV PATH=$PATH:/usr/local/go/bin  
  
WORKDIR $GOPATH  
  
# Setting up Golang workspace  
RUN mkdir bin \  
&& mkdir pkg \  
&& mkdir src  
  
# Installing gophercloud  
RUN cd src && go get github.com/gophercloud/gophercloud  
  
# Installing vim-go as IDE  
RUN git clone https://github.com/farazdagi/vim-go-ide.git ~/.vim_go_runtime &&
sh ~/.vim_go_runtime/bin/install \  
&& mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso
~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim \  
&& echo 'alias vimgo="vim -u ~/.vimrc.go"' >> ~/.bashrc \  
&& echo 'set t_Co=256' >> ~/.vimrc.go  


# docker-revel  
FROM golang  
MAINTAINER garbanzo <garbanzo.info@gmail.com>  
## Setting Vim  
RUN apt-get update  
RUN apt-get install -y vim  
RUN curl
https://raw.githubusercontent.com/Shougo/neobundle.vim/master/bin/install.sh >
install.sh  
RUN sh ./install.sh  
RUN rm ./install.sh  
ADD ./.vimrc /root/.vimrc  
## Install Revel  
RUN mkdir ~/gocode  
# export GOPATH=$GOPATH  
ENV GOPATH /gocode  
RUN echo 'export GOPATH=$GOPATH' >> ~/.bash_profile  
RUN /bin/bash -c "source ~/.bash_profile"  
RUN go get github.com/revel/revel  
RUN go get github.com/revel/cmd/revel  
RUN go get -u github.com/jinzhu/gorm  
# export PATH="$PATH:$GOPATH/bin"  
ENV PATH $PATH:$GOPATH/bin  
WORKDIR /gocode  
  


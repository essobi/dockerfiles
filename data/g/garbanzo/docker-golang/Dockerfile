FROM golang  
MAINTAINER garbanzo <garbanzo.info@gmail.com>  
RUN apt-get update  
RUN apt-get install -y vim  
RUN curl
https://raw.githubusercontent.com/Shougo/neobundle.vim/master/bin/install.sh >
install.sh  
RUN sh ./install.sh  
RUN rm ./install.sh  
ADD ./.vimrc /root/.vimrc  
WORKDIR /go  


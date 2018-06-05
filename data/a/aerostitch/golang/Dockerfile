FROM golang:latest  
  
Maintainer Joseph Herlant<herlantj@gmail.com>  
  
ENV GOPATH /go  
ENV PATH ${GOPATH}/bin:${PATH}  
  
COPY vimrc /root/.vimrc  
RUN apt update && apt install -y vim-nox git curl  
RUN mkdir -p ~/.vim/autoload ~/.vim/bundle \  
&& curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim \  
&& git clone https://github.com/fatih/vim-go.git ~/.vim/bundle/vim-go  
  
RUN go get -u github.com/golang/lint/golint \  
&& go install github.com/golang/lint/golint  
RUN go get -u github.com/axw/gocov/gocov \  
&& go install github.com/axw/gocov/gocov  
  
# Trick to make ycm work  
COPY testing.list /etc/apt/sources.list.d/testing.list  
COPY preferences /etc/apt/preferences  
RUN apt update && \  
apt install -y build-essential cmake python-dev python3-dev liblua5.2 vim-
nox/testing && \  
git clone https://github.com/Valloric/YouCompleteMe.git
~/.vim/bundle/YouCompleteMe  
RUN cd ~/.vim/bundle/YouCompleteMe && \  
git submodule update \--init --recursive && \  
./install.py \--gocode-completer  
  
WORKDIR ${GOPATH}/src  


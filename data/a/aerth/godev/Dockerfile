FROM golang:latest  
MAINTAINER aerth <aerth@riseup.net>  
RUN apt-get update && apt-get install -y \  
file \  
tree \  
gnupg \  
vim \  
vim-scripts \  
ca-certificates \  
locales \  
python3 \  
python3-setuptools \  
tmux \  
git  
# utf8  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
# asciinema  
RUN mkdir /usr/src/asciinema  
WORKDIR /usr/src/asciinema  
RUN git clone https://github.com/asciinema/asciinema .  
RUN python3 setup.py install  
  
# vim  
RUN mkdir -p /root/.vim/  
RUN curl -fLo /root/.vim/autoload/plug.vim --create-dirs
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim  
  
# vim-go  
RUN git clone https://github.com/fatih/vim-go.git /root/.vim/plugged/vim-go  
  
# Install vim-go stuff  
RUN echo "Getting go-vim dependencies"  
RUN apt-get install time  
RUN go get golang.org/x/tools/cmd/godoc && \  
go get github.com/nsf/gocode && \  
go get golang.org/x/tools/cmd/goimports && \  
go get github.com/rogpeppe/godef && \  
go get golang.org/x/tools/cmd/gorename && \  
go get github.com/golang/lint/golint && \  
go get github.com/kisielk/errcheck && \  
go get github.com/jstemmer/gotags  
  
ENV CGO_ENABLED 0  
RUN go get -v -d github.com/zyedidia/micro/cmd/micro  
WORKDIR /go/src/github.com/zyedidia/micro/  
RUN make && mv micro /go/bin/  
RUN mv -nv /go/bin/* /usr/local/bin/  
WORKDIR /root/  
RUN mkdir -p /root/.config/micro/plugins  
RUN git clone https://github.com/micro-editor/go-plugin
/root/.config/micro/plugins/go  
  
# IDE lol  
COPY bashrc /root/.bashrc  
COPY vimrc /root/.vimrc  
COPY microrc /root/.config/micro/settings.json  
  
ENV SHELL /bin/bash  
ENV PATH
/go/bin:/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
WORKDIR /go/  
CMD ["tmux"]


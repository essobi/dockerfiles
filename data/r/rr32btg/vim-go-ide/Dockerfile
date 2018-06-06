FROM golang  
  
# set env  
ENV HOME /home/dev  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
# install pagkages  
RUN apt-get update  
RUN apt-get install -y sudo ncurses-dev libtolua-dev exuberant-ctags pandoc
lynx  
  
RUN ln -s /usr/include/lua5.2/ /usr/include/lua  
RUN ln -s /usr/lib/x86_64-linux-gnu/liblua5.2.so /usr/lib/liblua.so  
  
# build and install vim  
RUN git clone https://github.com/vim/vim.git  
RUN cd vim && ./configure --with-features=huge --enable-luainterp --enable-
gui=no --without-x --prefix=/usr  
  
RUN cd vim && make -j`nproc` VIMRUNTIMEDIR=/usr/share/vim/vim74  
RUN cd vim && make install  
  
# get go tools  
RUN go get golang.org/x/tools/cmd/godoc  
RUN go get github.com/nsf/gocode  
RUN go get github.com/derekparker/delve/cmd/dlv  
RUN go get golang.org/x/tools/cmd/goimports  
RUN go get github.com/rogpeppe/godef  
RUN go get golang.org/x/tools/cmd/oracle  
RUN go get golang.org/x/tools/cmd/gorename  
RUN go get github.com/golang/lint/golint  
RUN go get github.com/kisielk/errcheck  
RUN go get github.com/jstemmer/gotags  
  
RUN curl https://glide.sh/get | sh  
  
RUN mv /go/bin/* /usr/local/go/bin  
  
# add dev user  
RUN mkdir -p /project  
  
RUN adduser dev --disabled-password --gecos ""  
RUN chown -R dev:dev $HOME /go /project  
RUN echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# cleanup  
RUN rm -rf /go/src/* /go/pkg  
  
RUN apt-get remove -y ncurses-dev  
RUN apt-get autoremove -y  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /vim  
  
USER dev  
  
# install pathogen  
RUN mkdir -p $HOME/.vim/autoload $HOME/.vim/bundle && \  
curl -LSso $HOME/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim  
  
# install vim plugins  
RUN git clone http://git@github.com/farazdagi/vim-go-ide.git
$HOME/.vim_go_runtime  
RUN sh $HOME/.vim_go_runtime/bin/install  
RUN mv $HOME/.vimrc.go $HOME/.vimrc  
# RUN vim +GoInstallBinaries +qall!  
VOLUME /project  
  
WORKDIR /project  
  
CMD /bin/bash -c /usr/bin/vim  


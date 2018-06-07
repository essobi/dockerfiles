FROM hoborg/ubuntu-dev-base:latest  
# pass in when building the image  
ARG PROXY=''  
# Proxies  
ENV http_proxy=$PROXY  
ENV https_proxy=$PROXY  
  
USER root  
  
# Download and install Go  
RUN curl https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz >
/tmp/go.tar.gz  
RUN tar -C /usr/local -xzf /tmp/go.tar.gz  
RUN rm /tmp/go.tar.gz  
  
# Switch back to user  
USER $USER  
# Neovim plugins + settings update  
RUN cd $HOME/.homesick/repos/dotvim && git pull  
RUN cd $HOME  
RUN nvim -c 'PlugInstall' || true  
RUN nvim -c 'PlugUpdate' || true  
RUN clear # clear terminal, nvim usually garbles it  
  
# Go environment variables  
ENV GOOS=linux  
ENV GOARCH=amd64  
ENV GOPATH=$HOME/shared/go  
  
COPY ./.zsh_aliases $HOME/.zsh_aliases  
  
# Install gocode daemon and static analysis tools  
RUN /usr/local/go/bin/go get -u github.com/nsf/gocode  
RUN /usr/local/go/bin/go get -u github.com/fzipp/gocyclo  
RUN /usr/local/go/bin/go get -u github.com/golang/lint/golint  
RUN /usr/local/go/bin/go get -u github.com/opennota/check/cmd/aligncheck  
RUN /usr/local/go/bin/go get -u github.com/opennota/check/cmd/structcheck  
RUN /usr/local/go/bin/go get -u github.com/opennota/check/cmd/varcheck  
RUN /usr/local/go/bin/go get -u github.com/kisielk/errcheck  
RUN /usr/local/go/bin/go get -u honnef.co/go/tools/cmd/megacheck  
RUN /usr/local/go/bin/go get -u github.com/mibk/dupl  
RUN /usr/local/go/bin/go get -u mvdan.cc/interfacer  
RUN /usr/local/go/bin/go get -u github.com/mdempsky/unconvert  
RUN /usr/local/go/bin/go get -u github.com/jgautheron/goconst/cmd/goconst  
RUN /usr/local/go/bin/go get -u github.com/tsenart/deadcode  
RUN /usr/local/go/bin/go get -u github.com/gordonklaus/ineffassign  
  
# Copy json sources for deoplete  
RUN mkdir -p $HOME/.cache/deoplete/go  
RUN cp -r "$HOME/.config/nvim/plugged/deoplete-
go/data/json/1.7.3/${GOOS}_${GOARCH}" \  
"$HOME/.cache/deoplete/go/"  
  
# Install go tools binaries required by vim-go  
RUN nvim -c 'GoInstallBinaries' || true # ignore errors  
  
CMD ["/usr/bin/zsh"]  


FROM alpine:edge  
  
MAINTAINER gurimusan <gurimusan@gmail.com>  
  
ENV LANG ja_JP.UTF-8  
ENV TIMEZONE Asia/Tokyo  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community/" >>
/etc/apk/repositories  
  
RUN apk add --update \  
file \  
git \  
zsh \  
openssh \  
tmux \  
xclip \  
sudo \  
less \  
curl \  
&& rm -rf /var/cache/* \  
&& mkdir /var/cache/apk  
  
RUN addgroup -g 1000 -S gurimusan \  
&& adduser -S gurimusan -u 1000 -G gurimusan \  
&& echo "gurimusan ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
COPY .zshrc /home/gurimusan/.zshrc  
COPY .gitconfig /home/gurimusan/.gitconfig  
  
RUN chown gurimusan:gurimusan /home/gurimusan/.zshrc  
RUN chown gurimusan:gurimusan /home/gurimusan/.gitconfig  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
RUN apk add --update --virtual build-deps \  
gcc \  
g++ \  
make \  
cmake \  
go \  
&& go get github.com/Masterminds/glide \  
&& mkdir /go/src/github.com/peco \  
&& cd /go/src/github.com/peco \  
&& git clone https://github.com/peco/peco.git \  
&& cd peco \  
&& /go/bin/glide install \  
&& go build -o /usr/local/bin/peco cmd/peco/peco.go \  
&& apk del build-deps \  
&& rm -rf /var/cache/* \  
&& mkdir /var/cache/apk \  
&& rm -fr /go  
  
USER gurimusan  
WORKDIR /home/gurimusan  
  
CMD ["/bin/zsh"]  


# All the Mutts - inspired by jess/mutt  
# TODO consume my vim container instead of installing vim  
# docker run -it \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v $HOME/.gnupg:/home/user/.gnupg \  
# -v $HOME/.mutt:/home/user/.mutt  
# -v $HOME/.vim:/home/user/.vim  
# -v $HOME/.vimrc:/home/user/.vimrc  
# --name mutt \  
# markhuge/mutt  
FROM alpine:edge  
  
MAINTAINER Mark Wilkerson <mark@markwilkerson.me>  
  
RUN addgroup -g 1000 user \  
&& adduser -D -h /home/user -G user -u 1000 user  
  
RUN apk --no-cache add \  
git autoconf gcc g++ make automake ncurses-dev openssl-dev \  
lynx vim cyrus-sasl-dev  
  
RUN git clone https://github.com/neomutt/neomutt.git /usr/src/neomutt  
  
WORKDIR /usr/src/neomutt  
  
RUN autoconf &>/dev/null; exit 0  
RUN autoreconf -vif  
RUN ./configure \  
\--with-mailpath=/home/user/.mutt/ \  
\--enable-imap \  
\--with-ssl \  
\--enable-sidebar \  
\--with-sasl \  
\--enable-smtp && \  
make && make install  
  
ENV BROWSER lynx  
  
USER user  
ENV HOME /home/user  
ENV TERM xterm-256color  
RUN mkdir $HOME/.mutt  
  
ENV LANG C.UTF-8  
CMD ["mutt", "-F", "~/.mutt/muttrc"]  


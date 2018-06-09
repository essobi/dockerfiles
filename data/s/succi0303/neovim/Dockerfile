FROM alpine:edge  
  
LABEL maintainer="succi0303@gmail.com"  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache \  
build-base \  
curl \  
gcc \  
git \  
grep \  
linux-headers \  
musl-dev\  
neovim \  
python-dev \  
py-pip \  
python3-dev \  
py3-pip \  
ruby \  
ruby-dev && \  
rm -rf /var/cache/apk/*  
  
ENV LANG="ja_JP.UTF-8" LANGUAGE="ja_JP:ja" LC_ALL="ja_JP.UTF-8"  
RUN pip3 install --upgrade pip neovim flake8 && \  
gem install --no-document etc json rubocop  
  
RUN curl -fLo /root/.local/share/nvim/site/autoload/plug.vim --create-dirs \  
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim  
  
COPY .config /root/.config  
  
RUN nvim +PlugInstall +qa  
  
WORKDIR /usr/src/nvim  
  
ENTRYPOINT ["nvim"]  


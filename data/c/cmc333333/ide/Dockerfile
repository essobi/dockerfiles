FROM node:6.2-slim  
MAINTAINER CM Lubinski <cm.lubinski@gmail.com>  
  
# Common packages  
RUN apt-get update \  
&& apt-get -y install git openssh-client vim \  
&& rm -rf /var/lib/apt/lists/*  
  
# Elm  
RUN npm install -g elm elm-oracle elm-test  
RUN curl -Lo /tmp/elm-format.tgz https://github.com/avh4/elm-
format/releases/download/0.4.0-alpha/elm-format-0.17-0.4.0-alpha-linux-x64.tgz
\  
&& cd /usr/bin \  
&& tar -xvzf /tmp/elm-format.tgz \  
&& rm /tmp/elm-format.tgz  
  
# Directory setup  
RUN mkdir -p /home/.vim/autoload /home/.vim/bundle /workdir  
  
# Plugins  
RUN curl -Lo /home/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim \  
&& cd /home/.vim/bundle \  
&& git clone \--depth=1 https://github.com/bling/vim-airline.git \  
&& git clone \--depth=1 https://github.com/ervandew/supertab.git \  
&& git clone \--depth=1 https://github.com/jwhitley/vim-matchit.git \  
&& git clone \--depth=1 https://github.com/scrooloose/nerdtree.git \  
&& git clone \--depth=1 https://github.com/scrooloose/syntastic.git \  
&& git clone \--depth=1 https://github.com/tpope/vim-commentary.git \  
&& git clone \--depth=1 https://github.com/tpope/vim-fugitive.git \  
&& git clone \--depth=1 https://github.com/tpope/vim-repeat.git \  
&& git clone \--depth=1 https://github.com/tpope/vim-speeddating.git \  
&& git clone \--depth=1 https://github.com/tpope/vim-surround.git \  
&& git clone \--depth=1 https://github.com/ElmCast/elm-vim.git  
  
COPY ["vimrc", "/home/.vimrc"]  
COPY ["gitconfig", "/home/.gitconfig"]  
COPY ["gitignore", "/home/.gitignore"]  
COPY ["entry.sh", "/home/entry.sh"]  
  
ENV TERM='xterm-256color' \  
PAGER='less' \  
EDITOR='vim'  
WORKDIR /workdir/  
ENTRYPOINT ["/home/entry.sh"]  


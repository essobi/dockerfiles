FROM alpine  
  
RUN apk add --no-cache vim git  
  
# pathogen installation:  
RUN mkdir -p /root/.vim/autoload /root/.vim/bundle  
ADD https://tpo.pe/pathogen.vim /root/.vim/autoload/pathogen.vim  
ADD .vimrc /root/.vimrc  
  
# vim plugins:  
WORKDIR /root/.vim/bundle  
RUN git clone git://github.com/tpope/vim-fugitive  
RUN git clone https://github.com/scrooloose/nerdtree  
RUN git clone https://github.com/scrooloose/syntastic  
RUN git clone https://github.com/bling/vim-airline  
RUN git clone https://github.com/fatih/vim-go  
  
# color scheme:  
RUN mkdir /root/.vim/colors  
ADD
https://raw.githubusercontent.com/nanotech/jellybeans.vim/master/colors/jellybeans.vim
/root/.vim/colors/jellybeans.vim  
  
RUN mkdir /src  
WORKDIR /src  
ENTRYPOINT ["vim"]  


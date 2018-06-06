FROM node  
MAINTAINER Matthew Pirocchi <matthew.pirocchi@gmail.com>  
  
# Install vim  
RUN apt-get update && apt-get install -y vim  
RUN echo "set tabstop=2 softtabstop=0 expandtab shiftwidth=2 smarttab" >>
~/.vimrc  
  
# Install Pathogen (vim module loader)  
RUN mkdir -p ~/.vim/autoload ~/.vim/bundle  
RUN curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim  
  
RUN echo "execute pathogen#infect()" >> ~/.vimrc  
RUN echo "syntax on" >> ~/.vimrc  
RUN echo "filetype plugin indent on" >> ~/.vimrc  
  
# Install vim-jsx (JSX syntax highlighting)  
RUN git clone https://github.com/mxw/vim-jsx.git ~/.vim/bundle/vim-jx  
RUN echo "let g:jsx_ext_required = 0" >> ~/.vimrc  
  
EXPOSE 8080  


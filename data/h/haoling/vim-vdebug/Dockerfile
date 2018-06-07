FROM haron/vim  
  
WORKDIR /home/dev  
RUN git clone https://github.com/gmarik/Vundle.vim.git .vim/bundle/Vundle.vim
&&\  
bash -c 'echo "set nocompatible" >> .vimrc' &&\  
bash -c 'echo "filetype off" >> .vimrc' &&\  
bash -c 'echo "set rtp+=~/.vim/bundle/Vundle.vim" >> .vimrc' &&\  
bash -c 'echo "call vundle#begin()" >> .vimrc' &&\  
bash -c 'echo "Plugin '"'"'gmarik/Vundle.vim'"'"'" >> .vimrc' &&\  
bash -c 'echo "Plugin '"'"'joonty/vdebug.git'"'"'" >> .vimrc' &&\  
bash -c 'echo "call vundle#end()" >> .vimrc' &&\  
bash -c 'echo "filetype plugin indent on" >> .vimrc' &&\  
vim +BundleInstall +qall  


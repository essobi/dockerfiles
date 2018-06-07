FROM kaggle/python  
ENV HOME /root  
WORKDIR /root  
  
## VIM-SLIME  
RUN apt-get install -y vim  
RUN mkdir -p ~/.vim/autoload ~/.vim/bundle && \  
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim  
  
COPY .vimrc /root/.vimrc  
COPY .screenrc /root/.screenrc  
  
RUN cd ~/.vim/bundle && \  
git clone git://github.com/jpalardy/vim-slime.git  
  
RUN apt-get install -y screen  
  


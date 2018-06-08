FROM debian:jessie  
  
RUN apt-get update && apt-get install vim-nox wget unzip git -y  
  
RUN mkdir ~/.vim && git clone https://github.com/flazz/vim-colorschemes.git
~/.vim  
  
COPY vimrc /root/.vimrc  
  
RUN git clone http://github.com/gmarik/vundle.git ~/.vim/bundle/vundle  
  
#RUN wget "https://raw.githubusercontent.com/yodiaditya/vim-
pydjango/master/.vimrc" -O /root/.vimrc  
#RUN echo | echo | vim +PluginInstall +qall &>/dev/null  
RUN echo | vim +PluginInstall +qall && \ || true  
  
RUN ls -lah /root/.vim/  
  
WORKDIR /root  
  


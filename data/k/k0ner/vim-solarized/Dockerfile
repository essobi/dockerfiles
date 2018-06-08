FROM jare/vim-bundle  
  
MAINTAINER k0ner <konradtendera@gmail.com>  
  
#add to .vimrc  
COPY vimrc /home/developer/my.vimrc  
  
RUN cat /home/developer/my.vimrc >> /home/developer/.vimrc~ \  
&& rm /home/developer/my.vimrc \  
&& sh /util/tidy-viml /home/developer/.vimrc~  


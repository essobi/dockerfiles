FROM ubuntu:14.04  
MAINTAINER mitsuchie "fsakura01@gmail.com"  
# install  
RUN apt-get update && apt-get upgrade  
  
# git  
RUN apt-get install git -y  
RUN apt-get install make -y  
  
# vim  
# RUN apt-get build-dep vim -y  
RUN apt-get install mercurial gettext libncurses5-dev libacl1-dev libgpm-dev
-y  
RUN apt-get install libperl-dev python-dev python3-dev ruby-dev -y  
RUN apt-get install lua5.2 liblua5.2-dev -y  
RUN apt-get install luajit libluajit-5.1 -y  
  
RUN hg clone https://vim.googlecode.com/hg/ vimbuild  
RUN cd /vimbuild && hg pull && hg update \  
&& ./configure --with-features=huge --enable-gui=gnome2 \  
\--enable-perlinterp --enable-pythoninterp \  
\--enable-python3interp --enable-rubyinterp \  
\--enable-luainterp --with-luajit \  
\--enable-fail-if-missing \  
\--prefix=/usr/local \  
&& make && sudo make install  
  
RUN cd /  
RUN rm -r /vimbuild  
  
RUN apt-get autoremove  


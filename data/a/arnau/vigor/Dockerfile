FROM debian:sid  
MAINTAINER Arnau Siches <asiches@gmail.com>  
  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
build-essential \  
git \  
locales \  
silversearcher-ag \  
vim-nox \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV TERM screen-256color  
  
COPY autoload /root/.vim/autoload  
COPY sections /root/.vim/sections  
COPY spell /root/.vim/spell  
COPY vimrc /root/.vimrc  
  
RUN mkdir -p /root/.vim/plugged \  
&& vim -c PlugInstall --not-a-term \  
&& find /root/.vim/plugged -name .git | xargs rm -rf  
  
WORKDIR /wd  
  
CMD ["vim"]  


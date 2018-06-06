FROM debian:jessie  
MAINTAINER Michael Faille <michael@faille.io>  
  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8
DEBIAN_FRONTEND=noninteractive HOME=/root  
  
RUN apt-get update && apt-get install -q -y --no-install-recommends locales &&
\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN dpkg-reconfigure locales && locale-gen C.UTF-8 && /usr/sbin/update-locale
LANG=C.UTF-8  
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
  
# Some usefull tools to work and debug docker  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https ca-certificates netcat iproute net-tools \  
vim-nox bash-completion curl gettext-base && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -o /usr/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64" && chmod +x
/usr/bin/gosu  
RUN /bin/echo -ne 'set nocompatible\nset backspace=eol,start,indent\nsyntax
on\nfiletype indent on\nset autoindent\ncolorscheme desert\nset
nobackup\nnnoremap ; :\n\n' > /etc/vim/vimrc.local  


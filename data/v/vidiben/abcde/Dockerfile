FROM alpine:3.7  
MAINTAINER Benoît Vidis <contact@benoitvidis.com>  
  
ENV EDITOR=vim  
ENV TERM=xterm-color  
  
RUN apk add --no-cache \  
abcde \  
cdparanoia \  
flac \  
lame \  
nano \  
py-eyed3 \  
vim \  
vorbis-tools \  
&& mkdir -p /abcde/out \  
&& echo "syntax on\nset expandtab ts=4 sw=4 autoindent encoding=utf8" >>
etc/vim/vimrc \  
&& echo done  
  
COPY abcde.conf /etc/abcde.conf  
  
ENTRYPOINT [ "abcde" ]  
  


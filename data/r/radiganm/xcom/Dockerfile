## Dockerfile for docker-xephyr-stumpwm  
##  
## Copyright 2016 Mac Radigan  
## All Rights Reserved  
FROM ubuntu:latest  
  
MAINTAINER Mac Radigan  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
## update APT  
RUN ulimit -n 1024  
RUN apt-get update --fix-missing  
  
## Xephyr + StumpWM  
RUN apt-get update && \  
apt-get install -y \  
curl \  
sudo \  
build-essential \  
autoconf \  
automake \  
git \  
xserver-xephyr \  
stumpwm \  
rxvt-unicode \  
texinfo \  
xterm \  
zsh \  
tmux \  
screen \  
vim \  
emacs \  
ack-grep \  
netbase \  
ncurses-dev \  
sbcl \  
firefox  
  
# # clean up APT  
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir -p /opt  
RUN (cd /opt; git clone https://github.com/radiganm/tecla.git && make -C
/opt/tecla -f bootstrap.mk install)  
  
RUN mkdir -p ~/local/github  
RUN (cd ~/local/github; git clone https://github.com/radiganm/slime.git)  
  
RUN (mkdir -p /tmp/quicklisp && curl -O
http://beta.quicklisp.org/quicklisp.lisp && /usr/bin/sbcl --load
quicklisp.lisp --eval '(quicklisp-quickstart:install)' \--eval '(ql:add-to-
init-file)' \--eval '(ql:quickload "clx")' \--eval '(ql:quickload "cl-ppcre")'
\--eval '(ql:quickload "alexandria")' \--eval '(ql:quickload "quicklisp-slime-
helper")' \--eval '(ql:quickload "split-sequence")' \--eval '(ql:quickload
"swank-client")' \--eval '(sb-ext:quit)' )  
COPY ./install-stumpwm.lisp /tmp  
RUN (cd /tmp; ./install-stumpwm.lisp)  
  
RUN curl -sSL
https://raw.githubusercontent.com/radiganm/environment/master/bootstrap/home.sh
| bash  
  
RUN (cd ~; rm -f .sbclrc .stumpwmrc)  
COPY ./home/ /opt/home/  
RUN (cd ~; ln -fs /opt/home/.s* .)  
  
# entry point  
ADD ./ctl /usr/bin  
RUN chmod 775 /usr/bin/ctl  
ENTRYPOINT ["/usr/bin/ctl"]  
  
## *EOF*  


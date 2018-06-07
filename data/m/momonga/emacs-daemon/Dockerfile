FROM debian:jessie  
MAINTAINER supermomonga  
  
## Install dependencies  
RUN apt-get update \  
&& apt-get install -y\  
autoconf\  
automake\  
libtool\  
texinfo\  
build-essential\  
xorg-dev\  
libgtk2.0-dev\  
libjpeg-dev\  
libncurses5-dev\  
libdbus-1-dev\  
libgif-dev\  
libtiff-dev\  
libm17n-dev\  
libpng12-dev\  
librsvg2-dev\  
libotf-dev\  
libxml2-dev\  
\  
git\  
&& rm -rf /var/lib/apt/lists/*  
  
## Install emacs  
RUN git clone \--depth 1 git://git.sv.gnu.org/emacs.git\  
&& cd emacs\  
&& ./autogen.sh\  
&& ./configure --with-x-toolkit=lucid\  
&& make bootstrap\  
&& make install  
  
ENV SERVER_NAME=emacs_server  
  
## TCP port  
EXPOSE 1234  
## Daemon server starting script  
COPY ./server.el /root/server.el  
  
## Directory to serve TCP connection auth file  
VOLUME /root/.emacs.d  
VOLUME /root/serverd  
  
## To execute apps easily using this image  
ONBUILD COPY ./app/ /root/app/  
  
## Run Emacs as a daemon  
CMD emacs --daemon --load=/root/server.el  


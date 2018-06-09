FROM phusion/baseimage:latest  
MAINTAINER Jonathan Ben-Joseph <jbenjos.work@gmail.com>  
CMD th -lgfx.go  
EXPOSE 8000  
ADD gfx_information.sh /usr/bin/gfx_information.sh  
  
RUN apt-get update && apt-get -y dist-upgrade  
RUN apt-get -y install libgraphicsmagick1-dev graphicsmagick wget npm nodejs
nodejs-legacy  
  
RUN wget -qO- https://raw.github.com/torch/ezinstall/master/install-deps |
bash  
RUN wget -qO- https://raw.github.com/torch/ezinstall/master/install-
luajit+torch | bash  
  
RUN git clone https://github.com/clementfarabet/torch-tutorials.git  
RUN git clone https://github.com/andresy/torch-demos.git  
  
RUN update-alternatives --install /usr/bin/xdg-open xdg-open
/usr/bin/gfx_information.sh 10  
  
RUN luarocks install
https://raw.github.com/clementfarabet/gfx.js/master/gfx.js-scm-0.rockspec  


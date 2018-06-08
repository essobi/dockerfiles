FROM base/archlinux  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN pacman -Sy --noconfirm  
RUN yes | pacman -S ipython python-pyzmq python-tornado python-nose python-
jinja python-pygments texlive-core mesa-libgl python-matplotlib python-numpy
python-pip wget  
  
ADD prep.sh /root/prep.sh  
RUN ipython profile create  
RUN sh /root/prep.sh  
RUN wget -O `ipython locate profile`/static/custom/custom.css
https://raw.githubusercontent.com/nsonnad/base16-ipython-
notebook/master/base16-solarized-dark.css  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
ADD start.sh /root/start.sh  
  
ENTRYPOINT sh /root/start.sh  


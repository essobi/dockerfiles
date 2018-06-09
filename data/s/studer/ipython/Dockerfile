# ipython notebook  
#  
# VERSION 3  
# use the studer archlinux base image  
FROM studer/arch  
  
MAINTAINER studer hello@studer.su  
  
# install ipython & dependencies  
RUN pacman -S --noconfirm ipython2 python2-tornado python2-jinja python2-pyzmq
python2-pip python2-scipy python2-pytz python2-dateutil freetype2  
  
# install matplotlib  
RUN pip2 install matplotlib  
  
# Launch ipython when launching the container  
ENTRYPOINT ["ipython2", "notebook", "--ip='0.0.0.0'", "--pylab", "inline"]  
  
# run ipython as the daemon user  
USER daemon  
  
# expose ipython port  
EXPOSE 8888  


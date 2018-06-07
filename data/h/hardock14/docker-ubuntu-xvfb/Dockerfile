# Firefox and Digikam over VNC  
#  
# Version 0.1  
FROM ubuntu:16.04  
# Install vnc, xvfb, firefox  
RUN apt-get update && apt-get install -y x11vnc xvfb ratpoison xterm firefox
software-properties-common locales  
RUN apt-get --reinstall install xfonts-base  
  
# set language  
RUN locale-gen de_DE.UTF-8  
RUN update-locale LANG=de_DE.UTF-8  
ENV LANG=de_DE.UTF-8  
# install Digikam5  
RUN add-apt-repository ppa:philip5/extra  
RUN apt-get update  
RUN apt-get install -y digikam5  
  
RUN mkdir ~/.vnc  
# Setup a password  
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd  
  
# start virtual framebuffer and ratpoison  
# RUN Xvfb -screen 0 1280x1024x16 -ac &  
RUN DISPLAY=:0 ratpoison &  
  
# Autostart firefox  
RUN bash -c 'echo "firefox" >> /.bashrc'  
  
EXPOSE 5900  
CMD ["x11vnc", "-forever", "-usepw", "-create"]  


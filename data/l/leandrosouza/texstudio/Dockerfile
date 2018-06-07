FROM harshjv/texlive-2015  
MAINTAINER Leandro Souza <leandrocsfrb@gmail.com>  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN locale-gen "en_US.UTF-8"  
RUN sudo dpkg-reconfigure locales  
  
RUN apt-get update  
  
RUN apt-get -f install -q -y ghostscript axel  
  
RUN apt-get install -q -y qt5-default qttools5-dev-tools libpoppler-qt5-1
libqt5script5 libqt5svg5  
  
WORKDIR $HOME  
  
RUN axel
http://download.opensuse.org/repositories/home:/jsundermeyer/xUbuntu_14.04/amd64/texstudio_2.11.0-1.1_amd64.deb  
  
RUN dpkg -i texstudio_2.11.0-1.1_amd64.deb  
  
RUN apt-get clean  
  
CMD texstudio  


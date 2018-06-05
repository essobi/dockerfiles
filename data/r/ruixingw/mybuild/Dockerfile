FROM ruixingw/dockbase  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
ARG ubuntuversion=xenial  
WORKDIR /tmp  
  
# git setting  
RUN git config --global push.default simple  
RUN git config --global user.name "ruixingw"  
RUN git config --global user.email "ruixingw@outlook.com"  
  
# Add source & update  
## emacs25 from https://launchpad.net/~kelleyk/+archive/ubuntu/emacs  
RUN echo "deb http://ppa.launchpad.net/kelleyk/emacs/ubuntu $ubuntuversion
main" >> /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/kelleyk/emacs/ubuntu $ubuntuversion
main" >> /etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EAAFC9CD  
## UPDATE  
RUN apt-get update  
  
## ambertools conda-build  
RUN conda install -q -y ambertools=17 -c
http://ambermd.org/downloads/ambertools/conda/  
## python packages  
RUN conda install -q -y -c anaconda numpy  
RUN conda install -q -y -c anaconda yaml  
  
## Source Code Pro  
RUN apt-get install -y fontconfig  
RUN mkdir -p /usr/share/fonts/opentype  
RUN wget --quiet https://github.com/adobe-fonts/source-code-
pro/archive/2.030R-ro/1.050R-it.tar.gz  
RUN tar xf 1.050R-it.tar.gz -C /usr/share/fonts/opentype/  
RUN fc-cache -f  
  
## spacemacs & python layer  
RUN apt-get install -y emacs25 dbus-x11  
RUN pip install autoflake flake8 yapf  
RUN pip install --upgrade "jedi>=0.9.0" "json-rpc>=1.8.1"
"service_factory>=0.1.5"  
ADD spacemacs /root/.spacemacs  
RUN git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d  
RUN emacs --daemon  
  
# Clean  
RUN apt-get clean  
RUN rm /tmp/* -rf  
  
# CMD sshd  
CMD ["/usr/sbin/sshd", "-D"]  
  


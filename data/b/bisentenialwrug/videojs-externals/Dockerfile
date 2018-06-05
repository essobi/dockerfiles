FROM ubuntu:16.04  
LABEL maintainer="LoveIsGrief"  
  
USER root  
  
RUN apt-get update -qqy  
RUN apt-get -qqy --no-install-recommends install wget bzip2 ca-certificates  
  
#=========  
# SSH server  
#=========  
RUN apt-get -qqy --no-install-recommends install openssh-server xauth  
RUN echo "X11UseLocalhost no" >> /etc/ssh/sshd_config  
  
#=========  
# User  
#=========  
RUN apt-get -qqy --no-install-recommends install git sudo  
ARG USER=vjs  
RUN useradd -m $USER  
RUN echo "$USER ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers.d/${USER}  
  
USER $USER  
WORKDIR /home/$USER  
  
RUN mkdir .ssh  
COPY id_rsa .ssh/  
COPY id_rsa.pub .ssh/authorized_keys  
RUN sudo chown -R $USER:$USER .ssh  
RUN chmod 0700 .ssh/  
RUN chmod 0600 .ssh/*  
  
# ====  
# nvm  
# ====  
ARG NODE_VERISON=6  
RUN wget -O nvm_v0.33.8.sh
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh  
RUN bash nvm_v0.33.8.sh  
RUN bash -lc "source ~/.profile && tail ~/.profile && nvm install
"$NODE_VERISON  
RUN bash -lc "source ~/.profile && npm install -g grunt-cli"  
  
#=========  
# Firefox  
#=========  
USER root  
RUN apt-get -qqy --no-install-recommends install firefox  
RUN apt-get -qqy install ubuntu-restricted-addons pulseaudio libpulse0  
ARG FIREFOX_VERSION=latest  
COPY firefox-installer.bash /tmp/  
RUN bash /tmp/firefox-installer.bash $FIREFOX_VERSION  
  
# TODO move this to firefox-local.Dockerfile  
#RUN git clone https://github.com/LoveIsGrief/videojs-externals.git  
#WORKDIR /home/${USER}/videojs-externals  
#RUN bash -lc 'source ~/.profile && nvm current && npm install'  
USER $USER  
CMD ["/bin/bash", "-l"]  


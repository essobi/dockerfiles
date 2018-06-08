FROM node  
  
MAINTAINER Rob Powell <rob.p.tec@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
git \  
wget \  
software-properties-common \  
python-software-properties \  
libgtk2.0-0 \  
tmux  
  
# Sublime  
RUN wget -O /tmp/sublime.deb http://c758482.r82.cf2.rackcdn.com/sublime-
text_build-3065_amd64.deb && \  
dpkg -i /tmp/sublime.deb && \  
rm /tmp/sublime.deb  
  
RUN adduser dev  
RUN echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
ENV HOME /home/dev  
  
WORKDIR ${HOME}  
  
RUN git clone \--depth=1 https://github.com/angular/material-start.git
material-starter  
  
WORKDIR ${HOME}/material-starter  
  
RUN chown -R dev:dev ${HOME}  
  
RUN npm install -g http-server bower && \  
npm install && \  
bower install --allow-root  
  
USER dev  
CMD ["/bin/bash"]


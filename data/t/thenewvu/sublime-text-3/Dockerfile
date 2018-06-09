FROM thenewvu/ubuntu-14.04  
MAINTAINER Vu Le "thenewvu@gmail.com"  
# prepare some app icon directories, this's required by sublime-text-3 setup  
RUN sudo mkdir -p /usr/share/icons/hicolor/16x16/apps/ && \  
sudo mkdir -p /usr/share/icons/hicolor/32x32/apps/ && \  
sudo mkdir -p /usr/share/icons/hicolor/48x48/apps/ && \  
sudo mkdir -p /usr/share/icons/hicolor/128x128/apps/ && \  
sudo mkdir -p /usr/share/icons/hicolor/256x256/apps/  
  
# install sublime-text-3 and needed packages  
RUN sudo add-apt-repository ppa:webupd8team/sublime-text-3 && \  
sudo apt-get update && \  
sudo apt-get install -y libgtk2.0-0 \  
libx11-6 \  
sublime-text-installer \  
git  
  
# setup a personal git configs  
COPY .gitconfig /home/vu/.gitconfig  
  
# clean up  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data/projects  
CMD subl  


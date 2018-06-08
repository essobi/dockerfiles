FROM ubuntu:14.04  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install and setup project dependencies  
RUN apt-get install -y curl wget  
RUN locale-gen en_US en_US.UTF-8  
  
#prepare for Java download  
RUN apt-get install -y python-software-properties  
RUN apt-get install -y software-properties-common  
  
#grab oracle java (auto accept licence)  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java7-installer  
  
# Install display server  
RUN apt-get install -y xorg xserver-xorg-video-dummy  
# RUN apt-get install -y xvfb gtk2-engines-pixbuf  
RUN apt-get install -y xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base
xfonts-scalable  
# RUN apt-get install -y x11-apps  
ADD xorg.conf /etc/X11/xorg.conf  
  
# Install Firefox  
RUN apt-get install -y firefox  
# Install Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
RUN apt-get update  
RUN apt-get install -y google-chrome-stable  
  
# Install maven  
RUN apt-get install -y maven  
  
# Define default command.  
CMD ["bash"]  
  


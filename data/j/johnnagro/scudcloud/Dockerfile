# Run scudcloud in a container  
#  
# https://github.com/raelgc/scudcloud  
#  
FROM ubuntu:16.04  
MAINTAINER John Nagro <john.nagro@gmail.com>  
  
RUN apt-get clean && apt-get update --fix-missing  
RUN apt-get install -y software-properties-common --no-install-recommends  
  
RUN apt-add-repository -y ppa:rael-gc/scudcloud  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections  
  
RUN apt-get clean && apt-get update --fix-missing  
RUN apt-get install -y \  
dbus \  
dbus-x11 \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libnotify-bin \  
notify-osd \  
scudcloud \  
hunspell-en-us \  
libqtwebkit-qupzillaplugins \  
python3-hunspell \  
\--no-install-recommends  
ENV DICTIONARY "en_US"  
CMD ["scudcloud"]  


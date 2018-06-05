FROM ubuntu:precise  
MAINTAINER hectord  
  
WORKDIR /root  
  
RUN echo deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu precise main >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y --force-yes python2.6-dev python2.6
tmux libxml2-dev libxslt1-dev libjpeg-dev libpng-dev libfreetype6-dev build-
essential wget pkg-config libpq-dev bzr git vim telnet net-tools unzip netcat-
openbsd xvfb  
  
RUN ln -f /usr/bin/python2.6 $(which python)  
  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
ADD requirements_unifield.txt ./  
RUN pip install -r requirements_unifield.txt  
  
RUN git clone https://github.com/wolfcw/libfaketime.git && cd libfaketime &&
make && make install  
  
RUN adduser --disabled-password --gecos "" testing  
USER testing  
  
WORKDIR /home/testing  
  
RUN bzr init-repo --no-trees repo  
  
USER root  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN apt-get update && apt-get install -y --allow-unauthenticated
postgresql-8.4  
  
RUN apt-get update && apt-get install -y expect  
  
ENTRYPOINT ["/home/testing/root-entrypoint.sh"]  
  
EXPOSE 8080  
EXPOSE 8006  
EXPOSE 8061  
VOLUME ["/output"]  
  
# Install some specific packages needed for Firefox 20.0 (installed below)  
RUN apt-get update && apt-get install -y libgtk2.0-0 libgtk-3-0 libasound2
libcanberra0 libdbus-glib-1-2 libdbusmenu-glib4 libdbusmenu-gtk4 libltdl7
libogg0 libstartup-notification0 libtdb1 libvorbis0a libvorbisfile3
libx11-xcb1 libxcb-util0 sound-theme-freedesktop  
  
USER testing  
  
RUN wget https://ftp.mozilla.org/pub/firefox/releases/20.0/linux-x86_64/en-
GB/firefox-20.0.tar.bz2  
RUN bunzip2 firefox-20.0.tar.bz2  
RUN tar -xvvf firefox-20.0.tar  
ENV PATH /home/testing/firefox:${PATH}  
  
  
ADD docker/docker-entrypoint.sh ./  
ADD docker/root-entrypoint.sh ./  
ADD docker/config.sh ./  
  
USER root  
  
ADD requirements.txt ./  
RUN pip install numpy==1.5.0  
RUN pip install -r requirements.txt  
  

